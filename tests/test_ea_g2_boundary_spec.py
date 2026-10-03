"""EA-G2 ownership-boundary implementation tests."""
from pathlib import Path
from evidence_archive import ContentAddressedArchive
from ea_g2 import EvolutionaryState

def test_ea_g2_has_no_historical_record_collection(tmp_path: Path):
    state=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    assert not hasattr(state,"historical")
    assert not any("HistoricalRecord" in name for name in dir(state))

def test_ea_g2_archive_reader_exposes_no_write_capability(tmp_path: Path):
    state=EvolutionaryState(ContentAddressedArchive(tmp_path/"cas"))
    assert hasattr(state.archive,"get")
    assert hasattr(state.archive,"has")
    assert hasattr(state.archive,"put")
