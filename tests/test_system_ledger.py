from evaluation.system_ledger import Ledger, Provenance, build_relationship, diagnose, reconcile_records

def prov(ref="fixture"):
    return Provenance(source_system="test", source_type="fixture", source_ref=ref, import_mode="READ_ONLY")

def test_hash_chain_and_status_separation(tmp_path):
    ledger = Ledger(tmp_path / "ledger.jsonl")
    first = ledger.append(record_id="sys-1", kind="system", status="OBSERVED", provenance=prov(), data={"name": "Example"})
    second = ledger.append(record_id="cap-1", kind="capability", status="NOT_MEASURED", provenance=prov(), data={"system_id": "sys-1"})
    assert first.record_hash
    assert second.previous_hash == first.record_hash
    assert ledger.verify_chain()["valid"] is True
    assert ledger.summary()["by_status"]["NOT_MEASURED"] == 1

def test_relationship_does_not_create_authority(tmp_path):
    ledger = Ledger(tmp_path / "ledger.jsonl")
    rel = build_relationship("kcn", "COMPOSES_WITH", "manifex", rationale="shared execution/evidence boundary")
    record = ledger.append(record_id="rel-1", kind="relationship", status="OBSERVED", authority="NONE", provenance=prov(), data=rel)
    assert record.authority == "NONE"

def test_reconciliation_is_non_mutating(tmp_path):
    a, b = Ledger(tmp_path / "a.jsonl"), Ledger(tmp_path / "b.jsonl")
    a.append(record_id="x", kind="artifact", status="OBSERVED", provenance=prov("a"), data={"sha": "1"})
    b.append(record_id="x", kind="artifact", status="OBSERVED", provenance=prov("b"), data={"sha": "2"})
    result = reconcile_records(a.records(), b.records())
    assert result["counts"]["CONFLICT"] == 1

def test_diagnostic_detects_unexecuted_test(tmp_path):
    ledger = Ledger(tmp_path / "ledger.jsonl")
    ledger.append(record_id="t1", kind="test", status="OBSERVED", provenance=prov(), data={})
    report = diagnose(ledger.records())
    assert any(g["type"] == "TEST_NOT_EXECUTED" for g in report["gaps"])
