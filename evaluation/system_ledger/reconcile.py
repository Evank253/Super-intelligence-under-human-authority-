"""Deterministic reconciliation and diagnostic analysis."""
from __future__ import annotations
from dataclasses import asdict
from typing import Any, Iterable
from .logger import LedgerRecord

def _index(rows: Iterable[LedgerRecord]) -> dict[str, LedgerRecord]:
    return {row.record_id: row for row in rows}

def reconcile_records(expected: Iterable[LedgerRecord], observed: Iterable[LedgerRecord]) -> dict[str, Any]:
    exp, obs = _index(expected), _index(observed)
    findings = []
    for record_id in sorted(set(exp) | set(obs)):
        if record_id not in obs:
            findings.append({"record_id": record_id, "status": "MISSING"})
            continue
        if record_id not in exp:
            findings.append({"record_id": record_id, "status": "UNEXPECTED"})
            continue
        a, b = exp[record_id], obs[record_id]
        differences = {}
        if a.kind != b.kind: differences["kind"] = {"expected": a.kind, "observed": b.kind}
        if a.status != b.status: differences["status"] = {"expected": a.status, "observed": b.status}
        if a.authority != b.authority: differences["authority"] = {"expected": a.authority, "observed": b.authority}
        if a.data != b.data: differences["data"] = {"expected": a.data, "observed": b.data}
        if a.provenance != b.provenance:
            differences["provenance"] = {"expected": asdict(a.provenance), "observed": asdict(b.provenance)}
        findings.append({
            "record_id": record_id,
            "status": "CONFLICT" if differences else "AGREEMENT",
            **({"differences": differences} if differences else {}),
        })
    counts = {}
    for finding in findings:
        counts[finding["status"]] = counts.get(finding["status"], 0) + 1
    return {"counts": dict(sorted(counts.items())), "findings": findings}

def diagnose(rows: Iterable[LedgerRecord]) -> dict[str, Any]:
    rows = list(rows)
    gaps = []
    tests = {r.record_id: r for r in rows if r.kind == "test"}
    runs = [r for r in rows if r.kind == "test_run"]
    scores = [r for r in rows if r.kind == "score"]
    artifacts = {r.record_id: r for r in rows if r.kind == "artifact"}
    run_test_ids = {r.data.get("test_id") for r in runs}
    for test_id in tests:
        if test_id not in run_test_ids:
            gaps.append({"type": "TEST_NOT_EXECUTED", "record_id": test_id})
    evidence_ids = {ref for score in scores for ref in score.data.get("evidence_refs", [])}
    for score in scores:
        if not score.data.get("evidence_refs"):
            gaps.append({"type": "SCORE_WITHOUT_EVIDENCE", "record_id": score.record_id})
    for ref in sorted(evidence_ids - artifacts.keys()):
        gaps.append({"type": "MISSING_EVIDENCE_ARTIFACT", "record_id": ref})
    record_ids = {r.record_id for r in rows}
    for row in rows:
        if row.status == "QUALIFIED":
            required = row.data.get("required_evidence_refs", [])
            missing = [x for x in required if x not in record_ids]
            if missing:
                gaps.append({"type": "QUALIFICATION_MISSING_PREREQUISITES", "record_id": row.record_id, "missing": missing})
    return {
        "records": len(rows), "tests": len(tests), "test_runs": len(runs),
        "scores": len(scores), "artifacts": len(artifacts),
        "gaps": gaps, "gap_count": len(gaps),
    }

def integration_opportunities(rows: Iterable[LedgerRecord]) -> list[dict[str, Any]]:
    return [
        {"relationship_id": row.record_id, **row.data}
        for row in rows
        if row.kind == "relationship"
        and row.data.get("relationship_type") in {"COMPOSES_WITH", "COMPLEMENTARY_TO"}
    ]
