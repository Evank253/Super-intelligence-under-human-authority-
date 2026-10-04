"""Append-only evidence-bounded system evaluation ledger."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import hashlib, json
from pathlib import Path
from typing import Any, Iterable

EVIDENCE_STATES = {
    "NOT_MEASURED", "UNRESOLVED", "HYPOTHESIZED", "INFERRED",
    "OBSERVED", "VERIFIED", "QUALIFIED", "SUPERSEDED",
}
AUTHORITY_STATES = {"NONE", "CANDIDATE", "AUTHORIZED", "RESTRICTED", "REVOKED"}
RELATIONSHIP_TYPES = {
    "DEPENDS_ON", "IMPLEMENTS", "TESTS", "VALIDATES", "PRODUCES_EVIDENCE",
    "EVIDENCE_FOR", "GOVERNED_BY", "ROUTES_TO", "FEEDS", "CONSUMES",
    "BLOCKED_BY", "CONTRADICTS", "DUPLICATES", "COMPOSES_WITH",
    "COMPLEMENTARY_TO", "BOTTLENECK_FOR", "SUPERSEDES", "DERIVED_FROM",
}

def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

@dataclass(frozen=True)
class Provenance:
    source_system: str
    source_type: str
    source_ref: str
    source_version: str | None = None
    commit_sha: str | None = None
    tree_sha: str | None = None
    file_path: str | None = None
    file_sha256: str | None = None
    imported_at: str = field(default_factory=utc_now)
    import_mode: str = "READ_ONLY"

    def validate(self) -> None:
        if not self.source_system or not self.source_ref:
            raise ValueError("provenance requires source_system and source_ref")
        if self.import_mode not in {"READ_ONLY", "COPIED", "GENERATED"}:
            raise ValueError("unsupported import_mode")

@dataclass(frozen=True)
class LedgerRecord:
    record_id: str
    kind: str
    status: str
    authority: str
    created_at: str
    provenance: Provenance
    data: dict[str, Any]
    previous_hash: str | None = None
    record_hash: str | None = None

    def payload(self) -> dict[str, Any]:
        body = asdict(self)
        body.pop("record_hash", None)
        return body

    def finalized(self) -> "LedgerRecord":
        if self.status not in EVIDENCE_STATES:
            raise ValueError(f"unknown evidence status: {self.status}")
        if self.authority not in AUTHORITY_STATES:
            raise ValueError(f"unknown authority status: {self.authority}")
        self.provenance.validate()
        digest = sha256_json(self.payload())
        return LedgerRecord(**{**asdict(self), "record_hash": digest})

class Ledger:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _last_hash(self) -> str | None:
        if not self.path.exists():
            return None
        last = None
        with self.path.open("r", encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    last = json.loads(line)["record_hash"]
        return last

    def append(self, *, record_id: str, kind: str, status: str,
               provenance: Provenance, data: dict[str, Any],
               authority: str = "NONE", created_at: str | None = None) -> LedgerRecord:
        previous_hash = self._last_hash()
        record = LedgerRecord(
            record_id=record_id, kind=kind, status=status, authority=authority,
            created_at=created_at or utc_now(), provenance=provenance,
            data=data, previous_hash=previous_hash,
        ).finalized()
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(canonical_json(asdict(record)) + "\n")
        return record

    def records(self) -> list[LedgerRecord]:
        if not self.path.exists():
            return []
        rows = []
        with self.path.open("r", encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    raw = json.loads(line)
                    raw["provenance"] = Provenance(**raw["provenance"])
                    rows.append(LedgerRecord(**raw))
        return rows

    def verify_chain(self) -> dict[str, Any]:
        rows = self.records()
        previous = None
        failures = []
        for index, row in enumerate(rows):
            if row.record_hash != sha256_json(row.payload()):
                failures.append({"index": index, "record_id": row.record_id, "reason": "HASH_MISMATCH"})
            if row.previous_hash != previous:
                failures.append({"index": index, "record_id": row.record_id, "reason": "CHAIN_BREAK"})
            previous = row.record_hash
        return {"records": len(rows), "valid": not failures, "failures": failures, "head_hash": previous}

    def summary(self) -> dict[str, Any]:
        rows = self.records()
        by_kind, by_status, by_authority = {}, {}, {}
        for row in rows:
            by_kind[row.kind] = by_kind.get(row.kind, 0) + 1
            by_status[row.status] = by_status.get(row.status, 0) + 1
            by_authority[row.authority] = by_authority.get(row.authority, 0) + 1
        return {
            "records": len(rows),
            "by_kind": dict(sorted(by_kind.items())),
            "by_status": dict(sorted(by_status.items())),
            "by_authority": dict(sorted(by_authority.items())),
            "chain": self.verify_chain(),
        }

def build_relationship(source_id: str, relationship_type: str, target_id: str,
                       *, rationale: str, evidence_refs: Iterable[str] = ()) -> dict[str, Any]:
    if relationship_type not in RELATIONSHIP_TYPES:
        raise ValueError(f"unsupported relationship type: {relationship_type}")
    return {
        "source_id": source_id, "relationship_type": relationship_type,
        "target_id": target_id, "rationale": rationale,
        "evidence_refs": list(evidence_refs),
    }
