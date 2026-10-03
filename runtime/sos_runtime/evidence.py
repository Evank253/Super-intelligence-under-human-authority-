from dataclasses import asdict
from .models import EvidenceRecord, new_id, now_iso

class EvidenceWitness:
    """Evidence witness. It records what is established and never grants authority."""
    def __init__(self, ledger):
        self.ledger = ledger
        self.records = {}

    def observe(self, subject_id, evidence_type, source, artifact_hash=None,
                disposition="OBSERVED", scope="UNSCOPED"):
        rec = EvidenceRecord(new_id("evidence"), subject_id, evidence_type, source,
                             now_iso(), artifact_hash, disposition, scope)
        self.records[rec.evidence_id] = rec
        self.ledger.append({"kind":"EVIDENCE_OBSERVED","timestamp":rec.observed_at,
                            "evidence":asdict(rec)})
        return rec
