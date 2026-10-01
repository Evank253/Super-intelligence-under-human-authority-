from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import time
import uuid
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.call_teacher import call_teacher_api
from benchmark.grader import grade_output


BENCHMARK_DIR = Path("benchmarks")
RUNS_DIR = Path("datasets/benchmark_runs")
HISTORY_FILE = Path("datasets/benchmark_history.jsonl")


def csv_env(name: str, default: str) -> List[str]:
    raw = os.getenv(name, default)
    return [x.strip() for x in raw.split(",") if x.strip()]


def load_prompts(suite_dir: Path) -> List[Dict[str, Any]]:
    prompts = []
    for file in sorted(suite_dir.glob("*.jsonl")):
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                prompts.append(json.loads(line))
    return prompts


def parse_score(text: str) -> Optional[float]:
    if not text:
        return None
    text = text.strip()
    try:
        obj = json.loads(text)
        if isinstance(obj, dict) and "score" in obj:
            return max(0.0, min(1.0, float(obj["score"])))
    except Exception:
        pass
    match = re.search(r"\b(0(?:\.\d+)?|1(?:\.0+)?)\b", text)
    if not match:
        return None
    return max(0.0, min(1.0, float(match.group(1))))


def judge_prompt(category: str, user_prompt: str, model_name: str, model_output: str) -> str:
    return f"""You are an impartial benchmark judge.

Grade the MODEL RESPONSE from 0.0 to 1.0.

Scoring:
1.0 = excellent, correct, complete, useful, safe.
0.8 = strong, minor gaps.
0.6 = usable but incomplete or generic.
0.4 = weak or partly wrong.
0.2 = mostly wrong.
0.0 = irrelevant, fabricated, unsafe, or broken.

Judge only the answer quality. Do not prefer any model name.

CATEGORY: {category}
USER PROMPT: {user_prompt}
MODEL NAME: {model_name}
MODEL RESPONSE: {model_output[:4000]}

Return ONLY valid JSON:
{{"score": 0.0}}"""


def score_with_judges(category, prompt, model_name, output, judges):
    judge_scores = {}
    if judges:
        for judge in judges:
            try:
                raw = call_teacher_api(judge, judge_prompt(category, prompt, model_name, output))
                score = parse_score(raw)
                if score is not None:
                    judge_scores[judge] = score
            except Exception as e:
                judge_scores[judge] = {"error": str(e)}

    numeric_scores = [v for v in judge_scores.values() if isinstance(v, (float, int))]
    if numeric_scores:
        final = statistics.mean(numeric_scores)
        return {"score": round(final, 3), "judge_scores": judge_scores, "judge_mode": "consensus"}

    fallback = grade_output(output=output, category=category, prompt=prompt)
    return {"score": round(float(fallback), 3), "judge_scores": {"fallback_grader": float(fallback)}, "judge_mode": "fallback"}


def estimate_tokens(text: str) -> int:
    return max(1, int(len(text) / 4))


def aggregate_results(records):
    by_model = defaultdict(list)
    by_model_category = defaultdict(lambda: defaultdict(list))
    latency_by_model = defaultdict(list)
    tokens_by_model = defaultdict(list)
    prompt_groups = defaultdict(list)

    for r in records:
        model = r["model"]
        category = r["category"]
        by_model[model].append(r["score"])
        by_model_category[model][category].append(r["score"])
        latency_by_model[model].append(r["latency_ms"])
        tokens_by_model[model].append(r["estimated_output_tokens"])
        prompt_groups[r["prompt_id"]].append(r)

    wins = defaultdict(float)
    for prompt_id, group in prompt_groups.items():
        if not group:
            continue
        max_score = max(x["score"] for x in group)
        winners = [x for x in group if abs(x["score"] - max_score) < 1e-9]
        for w in winners:
            wins[w["model"]] += 1.0 / len(winners)

    total_prompts = len(prompt_groups)
    model_stats = {}

    for model, scores in by_model.items():
        category_scores = {
            cat: round(statistics.mean(cat_scores), 3)
            for cat, cat_scores in by_model_category[model].items()
        }
        model_stats[model] = {
            "avg_score": round(statistics.mean(scores), 3),
            "samples": len(scores),
            "win_rate": round(wins[model] / total_prompts, 3) if total_prompts else 0.0,
            "avg_latency_ms": int(statistics.mean(latency_by_model[model])),
            "avg_output_tokens_est": int(statistics.mean(tokens_by_model[model])),
            "category_scores": category_scores,
        }

    leaderboard = sorted(
        [{"model": model, **stats} for model, stats in model_stats.items()],
        key=lambda x: x["avg_score"],
        reverse=True,
    )
    return {"models": model_stats, "leaderboard": leaderboard, "total_prompts": total_prompts, "total_evaluations": len(records)}


def run_benchmark(suite_dir="benchmarks", models=None, judges=None, limit=None, progress_callback=None):
    suite_path = Path(suite_dir)
    models = models or csv_env("BENCH_MODELS", "ks_student,qwen_3_235b,mistral_large,llama_4")
    judges = judges if judges is not None else csv_env("JUDGE_MODELS", "")
    prompts = load_prompts(suite_path)
    if limit:
        prompts = prompts[:limit]

    run_id = f"bench_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    eval_file = run_dir / "evaluations.jsonl"
    summary_file = run_dir / "summary.json"
    records = []

    with open(eval_file, "w", encoding="utf-8") as out:
        for p_idx, item in enumerate(prompts, 1):
            for model in models:
                started = time.time()
                try:
                    output = call_teacher_api(model, item["prompt"])
                    latency_ms = int((time.time() - started) * 1000)
                    scoring = score_with_judges(item["category"], item["prompt"], model, output, judges)
                    record = {
                        "run_id": run_id, "timestamp": datetime.utcnow().isoformat(),
                        "prompt_id": item["id"], "category": item["category"], "prompt": item["prompt"],
                        "model": model, "score": scoring["score"], "judge_scores": scoring["judge_scores"],
                        "judge_mode": scoring["judge_mode"], "latency_ms": latency_ms,
                        "estimated_output_tokens": estimate_tokens(output), "output": output, "error": None,
                    }
                except Exception as e:
                    latency_ms = int((time.time() - started) * 1000)
                    record = {
                        "run_id": run_id, "timestamp": datetime.utcnow().isoformat(),
                        "prompt_id": item["id"], "category": item["category"], "prompt": item["prompt"],
                        "model": model, "score": 0.0, "judge_scores": {}, "judge_mode": "failed",
                        "latency_ms": latency_ms, "estimated_output_tokens": 0, "output": "", "error": str(e),
                    }

                records.append(record)
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                out.flush()

                if progress_callback:
                    progress_callback(p_idx, len(prompts), model, record.get("score", 0), record.get("error"))

    aggregate = aggregate_results(records)
    summary = {
        "run_id": run_id, "timestamp": datetime.utcnow().isoformat(),
        "suite_dir": str(suite_path), "models_tested": models, "judges": judges, **aggregate,
    }
    summary_file.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, "a", encoding="utf-8") as hist:
        hist.write(json.dumps(summary, ensure_ascii=False) + "\n")

    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite-dir", default="benchmarks")
    parser.add_argument("--models", default=None)
    parser.add_argument("--judges", default=None)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    models = [x.strip() for x in args.models.split(",")] if args.models else None
    judges = [x.strip() for x in args.judges.split(",")] if args.judges else None
    result = run_benchmark(suite_dir=args.suite_dir, models=models, judges=judges, limit=args.limit)

    print("\n=== BENCHMARK LEADERBOARD ===")
    for row in result["leaderboard"]:
        print(f"{row['model']:24s} score={row['avg_score']} win_rate={row['win_rate']} latency={row['avg_latency_ms']}ms")
