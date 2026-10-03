"""BI-001 Building Index + Verification Machine foundation."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

class Status(str, Enum):
    ESTABLISHED = "ESTABLISHED"
    PARTIALLY_ESTABLISHED = "PARTIALLY_ESTABLISHED"
    NOT_ESTABLISHED = "NOT_ESTABLISHED"
    NOT_MEASURED = "NOT_MEASURED"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"

class ImplementationStatus(str, Enum):
    IMPLEMENTED = "IMPLEMENTED"
    PARTIAL = "PARTIAL"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    UNKNOWN = "UNKNOWN"

@dataclass(frozen=True)
class EvidenceRef:
    evidence_id: str
    source: str
    content_hash: str | None = None
    commit: str | None = None
    immutable: bool = True

@dataclass(frozen=True)
class StateVector:
    implementation: ImplementationStatus
    source_inspection: Status
    runtime_test: Status
    independent_evaluation: Status
    evidence_package: Status
    qualification: Status
    ratification: Status

@dataclass(frozen=True)
class ArtifactRecord:
    artifact_id: str
    name: str
    system_id: str
    origin: str
    creator: str | None
    created_at: str
    source: str | None
    commit: str | None
    tree_hash: str | None
    content_hash: str | None
    parent: str | None = None
    successor: str | None = None
    historical_record: bool = False
    frozen: bool = False
    evidence: tuple[EvidenceRef, ...] = field(default_factory=tuple)
    state: StateVector | None = None

class FrozenRecordError(ValueError):
    pass
class InvalidAuthorityOperation(ValueError):
    pass
class InvalidRecordError(ValueError):
    pass

class BuildingIndex:
    FORBIDDEN_OPERATIONS = frozenset({"authorize","grant_capability","qualify","approve","amend_constitution","override_human"})
    def __init__(self) -> None:
        self._records: dict[str, ArtifactRecord] = {}
        self._history: list[str] = []
    @property
    def records(self) -> Mapping[str, ArtifactRecord]:
        return dict(self._records)
    @property
    def history(self) -> tuple[str, ...]:
        return tuple(self._history)
    def register(self, record: ArtifactRecord) -> None:
        self._validate(record)
        if record.artifact_id in self._records:
            raise FrozenRecordError("existing artifact cannot be overwritten: " + record.artifact_id)
        self._records[record.artifact_id] = record
        self._history.append(record.artifact_id)
    def append_successor(self, record: ArtifactRecord, parent_id: str) -> None:
        parent = self._records.get(parent_id)
        if parent is None:
            raise KeyError(parent_id)
        if not (parent.frozen and parent.historical_record):
            raise InvalidRecordError("lineage parent must be frozen historical record")
        if record.parent != parent_id:
            raise InvalidRecordError("successor parent must reference frozen record")
        self.register(record)
    def attempt(self, operation: str) -> None:
        if operation in self.FORBIDDEN_OPERATIONS:
            raise InvalidAuthorityOperation("BI-001 cannot perform authority operation: " + operation)
        raise ValueError("unknown registry operation: " + operation)
    def compute_disposition(self, state: StateVector) -> Status:
        dims = (state.source_inspection, state.runtime_test, state.independent_evaluation, state.evidence_package)
        if Status.CONFLICT in dims:
            return Status.CONFLICT
        if state.runtime_test is Status.NOT_ESTABLISHED or state.independent_evaluation is Status.NOT_ESTABLISHED:
            return Status.NOT_ESTABLISHED
        if all(v is Status.ESTABLISHED for v in dims):
            return Status.ESTABLISHED
        if any(v in {Status.ESTABLISHED, Status.PARTIALLY_ESTABLISHED} for v in dims):
            return Status.PARTIALLY_ESTABLISHED
        if all(v in {Status.NOT_MEASURED, Status.UNKNOWN} for v in dims):
            return Status.NOT_MEASURED
        return Status.UNKNOWN
    def _validate(self, record: ArtifactRecord) -> None:
        required = {"artifact_id":record.artifact_id,"name":record.name,"system_id":record.system_id,"origin":record.origin,"created_at":record.created_at}
        missing = [k for k,v in required.items() if not v]
        if missing:
            raise InvalidRecordError("missing required fields: " + ", ".join(missing))
        if record.frozen and not record.historical_record:
            raise InvalidRecordError("frozen=True requires historical_record=True")
        if record.historical_record and not record.content_hash:
            raise InvalidRecordError("historical records require content_hash")
        if record.historical_record and not record.source:
            raise InvalidRecordError("historical records require source")
        if record.historical_record and not record.commit:
            raise InvalidRecordError("historical records require commit")

def build_gov003_pilot() -> tuple[BuildingIndex, ArtifactRecord, Status]:
    index = BuildingIndex()
    record = ArtifactRecord(
        artifact_id="RUNNER-GOV-003-INDEX-001",
        name="RUNNER-GOV-003 — Capability-Constrained Execution",
        system_id="KSI-EMERGENT-INTELLIGENCE",
        origin="DERIVED_FROM_PRIOR_WORK",
        creator="Evan Ketchum",
        created_at="2026-10-02",
        source="Evank253/KSI-Emergent-Intelligence",
        commit="56becf1392437dd8a80e82777c87060432df7293",
        tree_hash=None,
        content_hash=None,
        state=StateVector(
            implementation=ImplementationStatus.IMPLEMENTED,
            source_inspection=Status.ESTABLISHED,
            runtime_test=Status.ESTABLISHED,
            independent_evaluation=Status.ESTABLISHED,
            evidence_package=Status.PARTIALLY_ESTABLISHED,
            qualification=Status.NOT_ESTABLISHED,
            ratification=Status.NOT_ESTABLISHED,
        ),
        evidence=(EvidenceRef("GOV-003-AC-01-09","independent live-HEAD evaluation",commit="56becf1392437dd8a80e82777c87060432df7293"),),
    )
    index.register(record)
    return index, record, index.compute_disposition(record.state)  # type: ignore[arg-type]
