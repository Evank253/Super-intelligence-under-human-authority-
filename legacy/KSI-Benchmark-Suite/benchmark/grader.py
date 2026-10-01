"""
grader.py — heuristic fallback grader when no judge model is available.
Returns a float score 0.0–1.0.
"""
from __future__ import annotations

import re
from typing import Optional


CATEGORY_SIGNALS = {
    "code": {
        "positive": [r"def ", r"class ", r"import ", r"return ", r"```", r"function", r"try:", r"except"],
        "negative": [r"I cannot", r"I'm unable", r"As an AI"],
    },
    "reasoning": {
        "positive": [r"because", r"therefore", r"however", r"consider", r"tradeoff", r"example"],
        "negative": [r"I cannot", r"I'm unable"],
    },
    "math": {
        "positive": [r"\d+", r"=", r"formula", r"calculate", r"result", r"solution", r"\$"],
        "negative": [r"I cannot", r"I'm unable"],
    },
    "architecture": {
        "positive": [r"component", r"service", r"database", r"API", r"layer", r"scalab", r"deploy"],
        "negative": [r"I cannot", r"I'm unable"],
    },
    "business": {
        "positive": [r"strategy", r"market", r"customer", r"revenue", r"risk", r"metric", r"plan"],
        "negative": [r"I cannot", r"I'm unable"],
    },
}

MIN_WORDS = 30
GOOD_WORDS = 200


def grade_output(output: str, category: str, prompt: str) -> float:
    if not output or not output.strip():
        return 0.0

    words = len(output.split())
    if words < 5:
        return 0.05

    score = 0.0

    # Length signal (0–0.35)
    if words >= GOOD_WORDS:
        score += 0.35
    elif words >= MIN_WORDS:
        score += 0.20
    else:
        score += 0.05

    # Category signal (0–0.50)
    signals = CATEGORY_SIGNALS.get(category, {})
    pos = signals.get("positive", [])
    neg = signals.get("negative", [])

    pos_hits = sum(1 for p in pos if re.search(p, output, re.IGNORECASE))
    neg_hits = sum(1 for n in neg if re.search(n, output, re.IGNORECASE))

    if pos:
        score += 0.50 * (pos_hits / len(pos))

    if neg_hits:
        score -= 0.20 * neg_hits

    # Coherence signal (0–0.15): has sentence structure
    sentences = re.split(r'[.!?]+', output)
    non_empty = [s.strip() for s in sentences if len(s.strip()) > 10]
    if len(non_empty) >= 3:
        score += 0.15
    elif len(non_empty) >= 1:
        score += 0.05

    return max(0.0, min(1.0, score))
