from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List, Any


HISTORY_FILE = Path("datasets/benchmark_history.jsonl")
OUT_FILE = Path("datasets/replacement_recommendations.json")


def load_history() -> List[Dict[str, Any]]:
    if not HISTORY_FILE.exists():
        return []
    rows = []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def csv_env(name: str, default: str) -> List[str]:
    raw = os.getenv(name, default)
    return [x.strip() for x in raw.split(",") if x.strip()]


def recommend_replacements(student="ks_student", teachers=None, last_n=3, margin=0.0):
    history = load_history()
    teachers = teachers or csv_env("TEACHERS_TO_COMPARE", "qwen_3_235b,mistral_large,llama_4,qwen_coder")
    recommendations = []

    for teacher in teachers:
        comparisons = []
        for run in reversed(history):
            models = run.get("models", {})
            if student not in models or teacher not in models:
                continue
            student_score = float(models[student]["avg_score"])
            teacher_score = float(models[teacher]["avg_score"])
            comparisons.append({
                "run_id": run.get("run_id"),
                "timestamp": run.get("timestamp"),
                "student_score": student_score,
                "teacher_score": teacher_score,
                "delta": round(student_score - teacher_score, 4),
                "student_wins": student_score > teacher_score + margin,
            })
            if len(comparisons) >= last_n:
                break

        enough = len(comparisons) >= last_n
        should_replace = enough and all(c["student_wins"] for c in comparisons)

        recommendations.append({
            "teacher": teacher,
            "student": student,
            "enough_history": enough,
            "last_n": last_n,
            "margin": margin,
            "should_replace_teacher": should_replace,
            "comparisons": list(reversed(comparisons)),
        })

    result = {"student": student, "history_file": str(HISTORY_FILE), "recommendations": recommendations}
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--student", default="ks_student")
    parser.add_argument("--teachers", default=None)
    parser.add_argument("--last-n", type=int, default=3)
    parser.add_argument("--margin", type=float, default=0.0)
    args = parser.parse_args()

    teachers = [x.strip() for x in args.teachers.split(",")] if args.teachers else None
    result = recommend_replacements(student=args.student, teachers=teachers, last_n=args.last_n, margin=args.margin)
    print(json.dumps(result, indent=2, ensure_ascii=False))
