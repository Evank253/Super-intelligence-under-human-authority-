from pathlib import Path
import pytest
from evidence_archive import ContentAddressedArchive, HistoricalEvidenceReference
from ea_g2 import EvolutionaryState, Provenance, EvolutionRecord, ChallengeRecord, HumanRatificationRecord, AuthorityBoundaryError

def prov(): return Provenance("test","EA-G2","tests/test_ea_g2_runtime.py")

def test_runtime_has_no_historical_record_collection(tmp_path: Path):
    s=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    assert not hasattr(s, "historical")
    assert not any("HistoricalRecord" in n for n in dir(s))

def test_primary_reference_retrieval_is_verified(tmp_path: Path):
    a=ContentAddressedArchive(tmp_path/"cas"); d=a.put(b"evidence")
    s=EvolutionaryState(a)
    assert s.retrieve_verified(HistoricalEvidenceReference("EXP-004", __import__("evidence_archive").PrimaryIdentity("sha256-raw", d, "SHA-256", "raw-bytes", "primary"))) == b"evidence"

def test_wrong_hash_reference_is_rejected(tmp_path: Path):
    a=ContentAddressedArchive(tmp_path/"cas"); d=a.put(b"evidence")
    s=EvolutionaryState(a)
    r=EvolutionRecord("EV-1","EXP-004","0"*64,"old",("new evidence",),"new","reason","REFINEMENT",True,"NONE",prov())
    with pytest.raises(ValueError):
        s.add_evolution(r)

def test_evolution_requires_verifiable_historical_reference(tmp_path: Path):
    a=ContentAddressedArchive(tmp_path/"cas"); s=EvolutionaryState(a)
    r=EvolutionRecord("EV-1","EXP-004","a"*64,"old",("new evidence",),"new","reason","REFINEMENT",True,"NONE",prov())
    with pytest.raises(ValueError):
        s.add_evolution(r)

def test_state_collections_are_read_only_views(tmp_path: Path):
    s=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    with pytest.raises(TypeError):
        s.challenges["x"] = ChallengeRecord("C","EXP-004","UNRESOLVED",prov())

def test_authority_paths_fail_closed(tmp_path: Path):
    s=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    for method in (s.authorize_from_challenge,s.authorize_from_evidence,s.authorize_from_qualification,s.upgrade_from_consensus,s.modify_historical,s.modify_architecture_from_inside):
        with pytest.raises(AuthorityBoundaryError): method()

def test_direct_runtime_reassignment_is_rejected(tmp_path: Path):
    s=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    with pytest.raises(AttributeError): s._evolutions = {}

def test_records_are_immutable(tmp_path: Path):
    s=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    c=ChallengeRecord("C","EXP-004","NOT_MEASURED",prov())
    with pytest.raises((AttributeError,TypeError)): c.challenge_state="RESOLVED_SUPPORTED"

def test_ratification_is_explicit(tmp_path: Path):
    s=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    r=HumanRatificationRecord("R1","EV-1","RATIFIED","specific",(),"human decision",prov())
    s.add_ratification(r)
    assert "R1" in s.ratifications
