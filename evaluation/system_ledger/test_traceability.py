"""Adversarial tests for the Traceability & Recovery core.

Passing tests establish measured behavior only. They do not establish
qualification, authorization, or S4 authority.
"""
import pytest

from evaluation.system_ledger.traceability import (
    DependencyEdge,
    LineageRecord,
    RecoveryCandidate,
    TraceEngine,
    TraceRequest,
    TraceScope,
    TraceabilityDebt,
)


def req(target, **kwargs):
    return TraceRequest(
        request_id=f"req:{target}",
        target_id=target,
        scope=TraceScope(name="test", **kwargs),
    )


def test_TR_ADV_001_historical_work_is_recovered_not_rebuilt():
    engine = TraceEngine([{
        "record_id": "old-capability",
        "kind": "implementation",
        "source": "legacy-repo",
        "source_ref": "legacy-repo@abc123",
        "commit_sha": "abc123",
        "tree_sha": "tree123",
        "file_path": "src/capability.py",
        "temporal_state": "HISTORICAL",
        "trace_status": "FOUND",
    }])
    result = engine.trace(req("old-capability", include_historical=True))
    assert result.candidates[0].status == "RECOVERED"
    assert result.candidates[0].lineage.commit_sha == "abc123"
    assert result.authority == "NONE"
    assert "BUILD_NEW" not in str(result)


def test_TR_ADV_002_missing_information_is_not_global_absence():
    result = TraceEngine([]).trace(req("missing-artifact"))
    assert result.states == ("SEARCH_EXHAUSTED_FOR_SCOPE",)
    assert "global absence" in result.findings[0].message
    assert result.authority == "NONE"


def test_TR_ADV_003_recursive_evidence_debt():
    engine = TraceEngine([
        {"record_id": "cap", "kind": "capability", "dependencies": ["impl"]},
        {"record_id": "impl", "kind": "implementation", "dependencies": ["test"]},
        {"record_id": "test", "kind": "test", "dependencies": ["evidence-a"]},
        {"record_id": "evidence-a", "kind": "artifact", "dependencies": ["artifact-b"]},
        {"record_id": "artifact-b", "kind": "artifact", "dependencies": ["dataset-c"]},
    ])
    result = engine.trace_dependencies("cap")
    assert {f.target_id for f in result.findings if f.state == "MISSING"} == {"dataset-c"}
    assert len(result.debt) == 1
    assert result.debt[0].missing_ids == ("dataset-c",)
    assert result.authority == "NONE"


def test_TR_ADV_004_authority_isolation():
    engine = TraceEngine([{
        "record_id": "verified-history",
        "kind": "artifact",
        "source": "legacy",
        "source_ref": "legacy@v1",
        "temporal_state": "HISTORICAL",
        "trace_status": "RECOVERED",
    }])
    result = engine.trace(req("verified-history", include_historical=True))
    assert result.authority == "NONE"
    assert all(f.authority == "NONE" for f in result.findings)
    assert all(c.status != "QUALIFIED" for c in result.candidates)


def test_cycle_terminates_without_infinite_traversal():
    engine = TraceEngine([
        {"record_id": "a", "dependencies": ["b"]},
        {"record_id": "b", "dependencies": ["a"]},
    ])
    result = engine.trace_dependencies("a")
    assert any(f.state == "UNRESOLVED" and "cycle" in f.message for f in result.findings)
    assert result.authority == "NONE"


def test_historical_scope_is_required():
    engine = TraceEngine([{
        "record_id": "old",
        "kind": "implementation",
        "temporal_state": "HISTORICAL",
    }])
    result = engine.trace(req("old"))
    assert result.states == ("SEARCH_EXHAUSTED_FOR_SCOPE",)


def test_lineage_requires_provenance_identity():
    with pytest.raises(ValueError):
        LineageRecord("", "repo", "ref").validate()


def test_traceability_debt_cannot_carry_authority():
    with pytest.raises(ValueError):
        TraceabilityDebt("d", "x", ("y",), "missing", authority="AUTHORIZED")


def test_recovery_candidate_validates_state():
    lineage = LineageRecord("x", "repo", "ref")
    with pytest.raises(ValueError):
        RecoveryCandidate("x", "implementation", "INVALID", lineage)


def test_dependency_edge_requires_endpoints():
    with pytest.raises(ValueError):
        DependencyEdge("", "target")
