"""Generate explicit system evaluation checklist from ledger state."""
from __future__ import annotations
from typing import Iterable, Any
from .logger import LedgerRecord

def checklist(rows: Iterable[LedgerRecord]) -> list[dict[str, Any]]:
    rows = list(rows)
    kinds = {r.kind for r in rows}
    return [
        {"id": "ARCH-001", "area": "architecture", "item": "Architecture recorded", "status": "DONE" if "system" in kinds else "MISSING"},
        {"id": "CAP-001", "area": "capability", "item": "Capabilities enumerated", "status": "DONE" if "capability" in kinds else "MISSING"},
        {"id": "IMP-001", "area": "implementation", "item": "Implementation records exist", "status": "DONE" if "implementation" in kinds else "MISSING"},
        {"id": "TEST-001", "area": "testing", "item": "Tests registered", "status": "DONE" if "test" in kinds else "MISSING"},
        {"id": "RUN-001", "area": "testing", "item": "Executed test runs recorded", "status": "DONE" if "test_run" in kinds else "MISSING"},
        {"id": "SCORE-001", "area": "measurement", "item": "Scores recorded", "status": "DONE" if "score" in kinds else "MISSING"},
        {"id": "ART-001", "area": "evidence", "item": "Evidence artifacts recorded", "status": "DONE" if "artifact" in kinds else "MISSING"},
        {"id": "REL-001", "area": "integration", "item": "System relationships recorded", "status": "DONE" if "relationship" in kinds else "MISSING"},
        {"id": "REC-001", "area": "reconciliation", "item": "Reconciliation ready", "status": "READY" if "artifact" in kinds else "PENDING"},
        {"id": "DIAG-001", "area": "diagnostic", "item": "Gap analysis ready", "status": "READY" if rows else "PENDING"},
        {"id": "GOV-001", "area": "governance", "item": "Human authority remains separate", "status": "DESIGN_CONSTRAINT"},
    ]
