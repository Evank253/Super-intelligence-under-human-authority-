"""Executable EA-G2 adversarial suite.

These tests measure implementation behavior only. Passing tests are not
qualification, truth, authority, or superintelligence claims.
"""
from pathlib import Path
import hashlib
import pytest

from evidence_archive import ContentAddressedArchive, HistoricalEvidenceReference, PrimaryIdentity, SecondaryIdentifier
from ea_g2 import EvolutionaryState, Provenance, EvolutionRecord, ChallengeRecord, HumanRatificationRecord, AuthorityBoundaryError, HistoricalReferenceError

def P(): return Provenance("adversarial-test", "EA-G2", __file__)
def state(tmp_path: Path):
    archive = ContentAddressedArchive(tmp_path / "cas")
    return archive, EvolutionaryState(archive)

def ref(record_id, data=b"historical"):
    digest = hashlib.sha256(data).hexdigest()
    return HistoricalEvidenceReference(record_id, PrimaryIdentity("sha256-raw", digest, "SHA-256", "raw-bytes", "primary"), provenance=P())

def evolution(h, data=b"historical"):
    return EvolutionRecord("EV-1", h.record_id, h.content_hash, "old", ("new evidence",), "new", "reason", "REFINEMENT", True, "NONE", P())

# G2-01
def test_g2_01_runtime_has_no_archive_write_capability(tmp_path):
    archive, s = state(tmp_path)
    assert not hasattr(s, "historical")
    with pytest.raises(AuthorityBoundaryError): s.archive.put(b"forbidden")
    assert not hasattr(s, "_archive")

# G2-02
def test_g2_02_corrupt_cas_fails_closed(tmp_path):
    archive, s = state(tmp_path)
    data=b"evidence"; digest=archive.put(data)
    path=archive._path_for(digest); path.write_bytes(b"tampered")
    with pytest.raises(HistoricalReferenceError): s.retrieve_verified(ref("EXP-1", data))

# G2-03
def test_g2_03_wrong_hash_reference_rejected(tmp_path):
    archive, s = state(tmp_path); archive.put(b"evidence")
    bad=ref("EXP-1", b"different")
    with pytest.raises(HistoricalReferenceError): s.retrieve_verified(bad)

# G2-04
def test_g2_04_historical_overwrite_paths_rejected(tmp_path):
    archive, s = state(tmp_path)
    with pytest.raises(AuthorityBoundaryError): s.modify_historical("EXP-1", b"changed")
    assert not hasattr(s, "historical")

# G2-05
def test_g2_05_authority_boundary_direct_assignment_rejected(tmp_path):
    _, s = state(tmp_path)
    with pytest.raises(AttributeError): s.authority_boundary = "INTERNAL_SYSTEM"

# G2-06
def test_g2_06_guard_replacement_does_not_mutate_bound_method_surface(tmp_path):
    _, s = state(tmp_path)
    with pytest.raises(AttributeError): s.authorize_from_evidence = lambda: None

# G2-07
def test_g2_07_evolution_record_is_immutable(tmp_path):
    archive, s = state(tmp_path); r=ref("EXP-1"); archive.put(b"historical")
    e=evolution(r); s.add_evolution(e)
    with pytest.raises((AttributeError, TypeError)): e.historical_record_preserved=False
    assert s.evolutions["EV-1"].historical_impact == "NONE"

# G2-08
def test_g2_08_qualification_cannot_create_authority(tmp_path):
    _, s = state(tmp_path)
    with pytest.raises(AuthorityBoundaryError): s.authorize_from_qualification("QUALIFIED")

# G2-09
def test_g2_09_consensus_cannot_create_truth(tmp_path):
    _, s = state(tmp_path)
    with pytest.raises(AuthorityBoundaryError): s.upgrade_from_consensus(["A","B"])

# G2-10
def test_g2_10_missing_provenance_rejected(tmp_path):
    _, s = state(tmp_path)
    with pytest.raises(Exception):
        s.add_challenge(ChallengeRecord("C-1", "EXP-1", "UNRESOLVED", None))

# G2-11
def test_g2_11_evolution_requires_verifiable_traceability(tmp_path):
    archive, s = state(tmp_path)
    bad=EvolutionRecord("EV-1","EXP-1","a"*64,"old",("new evidence",),"new","reason","REFINEMENT",True,"NONE",P())
    with pytest.raises(HistoricalReferenceError): s.add_evolution(bad)

# G2-12
def test_g2_12_ratification_is_explicit_and_non_authoritative(tmp_path):
    _, s = state(tmp_path)
    r=HumanRatificationRecord("R-1","EV-1","RATIFIED","EV-1",(),"human decision",P())
    s.add_ratification(r)
    assert s.ratifications["R-1"].decision == "RATIFIED"
    with pytest.raises(AuthorityBoundaryError): s.authorize_from_challenge("R-1")

def test_secondary_identifier_requires_explicit_primary_verification(tmp_path):
    _, _ = state(tmp_path)
    with pytest.raises(ValueError):
        SecondaryIdentifier("ipfs-cid","bafyexample","multihash","dag-cbor","secondary","none",False,"2026-10-03T00:00:00Z")

def test_secondary_identifier_is_additive_and_typed():
    sec=SecondaryIdentifier("ipfs-cid","bafyexample","multihash","raw-bytes","secondary","recompute-sha256","true","2026-10-03T00:00:00Z")
    assert sec.identifier_type == "ipfs-cid"
