"""Small, evidence-bounded Traceability & Recovery core.

This module discovers and reconstructs lineage from caller-supplied records. It
never grants qualification, authorization, ratification, or S4 authority.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

TRACE_STATES = {
    "FOUND", "RECOVERED", "SEARCH_EXHAUSTED_FOR_SCOPE", "MISSING",
    "UNRESOLVED", "CONFLICTING", "SUPERSEDED", "IMPLEMENTED_UNMEASURED",
    "EVIDENCE_GAP", "TRACEABILITY_DEBT",
}
NON_AUTHORITY = "NONE"


@dataclass(frozen=True)
class TraceScope:
    name: str
    sources: tuple[str, ...] = ()
    include_historical: bool = False
    include_related: bool = False
    include_superseded: bool = False
    include_moved: bool = False
    include_partial: bool = False

    def contains(self, source: str) -> bool:
        return not self.sources or source in self.sources


@dataclass(frozen=True)
class TraceRequest:
    request_id: str
    target_id: str
    scope: TraceScope
    purpose: str = "trace"


@dataclass(frozen=True)
class LineageRecord:
    record_id: str
    source_system: str
    source_ref: str
    commit_sha: str | None = None
    tree_sha: str | None = None
    file_path: str | None = None
    file_sha256: str | None = None
    temporal_state: str = "CURRENT"

    def validate(self) -> None:
        if not self.record_id or not self.source_system or not self.source_ref:
            raise ValueError("lineage requires record_id, source_system, source_ref")
        if self.temporal_state not in {"CURRENT", "HISTORICAL", "SUPERSEDED"}:
            raise ValueError("invalid temporal_state")


@dataclass(frozen=True)
class RecoveryCandidate:
    record_id: str
    kind: str
    status: str
    lineage: LineageRecord
    limitations: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in TRACE_STATES:
            raise ValueError(f"invalid recovery status: {self.status}")
        self.lineage.validate()


@dataclass(frozen=True)
class TraceFinding:
    finding_id: str
    state: str
    target_id: str
    message: str
    dependency_ids: tuple[str, ...] = ()
    candidate_ids: tuple[str, ...] = ()
    authority: str = NON_AUTHORITY

    def __post_init__(self) -> None:
        if self.state not in TRACE_STATES:
            raise ValueError(f"invalid trace state: {self.state}")
        if self.authority != NON_AUTHORITY:
            raise ValueError("traceability findings cannot carry authority")


@dataclass(frozen=True)
class DependencyEdge:
    source_id: str
    target_id: str
    relationship: str = "DEPENDS_ON"

    def __post_init__(self) -> None:
        if not self.source_id or not self.target_id:
            raise ValueError("dependency edge requires source and target")


@dataclass(frozen=True)
class TraceabilityDebt:
    debt_id: str
    target_id: str
    missing_ids: tuple[str, ...]
    reason: str
    authority: str = NON_AUTHORITY

    def __post_init__(self) -> None:
        if not self.missing_ids:
            raise ValueError("traceability debt requires missing_ids")
        if self.authority != NON_AUTHORITY:
            raise ValueError("traceability debt cannot carry authority")


@dataclass(frozen=True)
class TraceResult:
    request: TraceRequest
    findings: tuple[TraceFinding, ...]
    candidates: tuple[RecoveryCandidate, ...] = ()
    debt: tuple[TraceabilityDebt, ...] = ()
    authority: str = NON_AUTHORITY

    def __post_init__(self) -> None:
        if self.authority != NON_AUTHORITY:
            raise ValueError("trace results cannot carry authority")

    @property
    def states(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys(f.state for f in self.findings))


class TraceEngine:
    """Deterministic trace engine over an immutable in-memory record index.

    Records are mappings with at least record_id, kind, and data.
    Optional source, temporal_state, dependencies, and related_ids fields are
    used for scope and lineage analysis.
    """

    def __init__(self, records: Iterable[Mapping]):
        self._records = {
            str(r["record_id"]): dict(r)
            for r in records
            if "record_id" in r
        }

    def _eligible(self, record: Mapping, scope: TraceScope) -> bool:
        source = str(record.get("source", ""))
        if not scope.contains(source):
            return False
        temporal = record.get("temporal_state", "CURRENT")
        if temporal == "HISTORICAL" and not scope.include_historical:
            return False
        if temporal == "SUPERSEDED" and not scope.include_superseded:
            return False
        if record.get("moved") and not scope.include_moved:
            return False
        if record.get("partial") and not scope.include_partial:
            return False
        return True

    def search(self, request: TraceRequest) -> tuple[Mapping, ...]:
        return tuple(
            self._records[rid]
            for rid in sorted(self._records)
            if self._eligible(self._records[rid], request.scope)
            and (
                rid == request.target_id
                or request.target_id in self._records[rid].get("aliases", [])
                or request.target_id in self._records[rid].get("related_ids", [])
            )
        )

    def trace(self, request: TraceRequest) -> TraceResult:
        matches = self.search(request)
        if not matches:
            finding = TraceFinding(
                finding_id=f"{request.request_id}:search",
                state="SEARCH_EXHAUSTED_FOR_SCOPE",
                target_id=request.target_id,
                message="No eligible record found in the requested scope; global absence is not established.",
            )
            return TraceResult(request=request, findings=(finding,))

        candidates = tuple(self._candidate(r) for r in matches)
        findings = tuple(
            TraceFinding(
                finding_id=f"{request.request_id}:found:{c.record_id}",
                state=c.status,
                target_id=request.target_id,
                message="Trace candidate located with recorded provenance; current validity remains separate.",
                candidate_ids=(c.record_id,),
            )
            for c in candidates
        )
        return TraceResult(request=request, findings=findings, candidates=candidates)

    def _candidate(self, record: Mapping) -> RecoveryCandidate:
        data = record.get("data", {})
        lineage = LineageRecord(
            record_id=str(record["record_id"]),
            source_system=str(record.get("source_system", record.get("source", "unknown"))),
            source_ref=str(record.get("source_ref", record["record_id"])),
            commit_sha=record.get("commit_sha"),
            tree_sha=record.get("tree_sha"),
            file_path=record.get("file_path"),
            file_sha256=record.get("file_sha256"),
            temporal_state=str(record.get("temporal_state", "CURRENT")),
        )
        status = str(record.get("trace_status", "FOUND"))
        if status == "FOUND" and lineage.temporal_state == "HISTORICAL":
            status = "RECOVERED"
        return RecoveryCandidate(
            record_id=str(record["record_id"]),
            kind=str(record.get("kind", "unknown")),
            status=status,
            lineage=lineage,
            limitations=tuple(data.get("limitations", record.get("limitations", ()))),
            dependencies=tuple(data.get("dependencies", record.get("dependencies", ()))),
        )

    def trace_dependencies(self, root_id: str, max_nodes: int = 1000) -> TraceResult:
        request = TraceRequest(
            request_id=f"dependency:{root_id}",
            target_id=root_id,
            scope=TraceScope("dependency"),
        )
        if root_id not in self._records:
            return self.trace(request)

        findings: list[TraceFinding] = []
        debt: list[TraceabilityDebt] = []
        seen: set[str] = set()
        active: set[str] = set()
        missing: set[str] = set()

        def walk(node_id: str) -> None:
            if len(seen) >= max_nodes:
                findings.append(TraceFinding(
                    finding_id=f"dependency:limit:{node_id}",
                    state="UNRESOLVED",
                    target_id=node_id,
                    message="Dependency traversal limit reached; trace is incomplete.",
                ))
                return
            if node_id in active:
                findings.append(TraceFinding(
                    finding_id=f"dependency:cycle:{node_id}",
                    state="UNRESOLVED",
                    target_id=node_id,
                    message="Dependency cycle detected; traversal terminated at the repeated node.",
                ))
                return
            if node_id in seen:
                return
            seen.add(node_id)
            active.add(node_id)
            record = self._records[node_id]
            deps = tuple(record.get("dependencies", record.get("data", {}).get("dependencies", ())))
            for dep_id in deps:
                dep_id = str(dep_id)
                if dep_id not in self._records:
                    missing.add(dep_id)
                    findings.append(TraceFinding(
                        finding_id=f"dependency:missing:{node_id}:{dep_id}",
                        state="MISSING",
                        target_id=dep_id,
                        message=f"Dependency required by {node_id} is not established in the trace index.",
                        dependency_ids=(node_id,),
                    ))
                else:
                    walk(dep_id)
            active.remove(node_id)

        walk(root_id)
        if missing:
            debt.append(TraceabilityDebt(
                debt_id=f"debt:{root_id}",
                target_id=root_id,
                missing_ids=tuple(sorted(missing)),
                reason="Recovered dependency chain contains unestablished downstream dependencies.",
            ))
            findings.append(TraceFinding(
                finding_id=f"dependency:debt:{root_id}",
                state="TRACEABILITY_DEBT",
                target_id=root_id,
                message="Dependency traversal exposed missing downstream information; no substitute was generated.",
                dependency_ids=tuple(sorted(missing)),
            ))
        elif not findings:
            findings.append(TraceFinding(
                finding_id=f"dependency:complete:{root_id}",
                state="FOUND",
                target_id=root_id,
                message="Dependency traversal completed without an observed missing dependency.",
            ))
        return TraceResult(request=request, findings=tuple(findings), debt=tuple(debt))


def trace_before_build(engine: TraceEngine, request: TraceRequest) -> TraceResult:
    return engine.trace(request)


def preserve_gap(engine: TraceEngine, request: TraceRequest) -> TraceResult:
    return engine.trace(request)
