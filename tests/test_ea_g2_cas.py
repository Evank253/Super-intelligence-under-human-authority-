from pathlib import Path

import pytest

from evidence_archive import ContentAddressedArchive, IntegrityError, HistoricalEvidenceReference


def test_cas_round_trip_and_hash_verification(tmp_path: Path):
    archive = ContentAddressedArchive(tmp_path / "cas")
    data = b"historical-evidence"
    digest = archive.put(data)
    assert archive.get(digest) == data
    assert archive.has(digest)
    ref = HistoricalEvidenceReference("EXP-004", digest)
    assert ref.content_hash == digest


def test_cas_detects_corruption(tmp_path: Path):
    archive = ContentAddressedArchive(tmp_path / "cas")
    digest = archive.put(b"original")
    path = tmp_path / "cas" / digest[:2] / digest
    path.write_bytes(b"tampered")
    with pytest.raises(IntegrityError):
        archive.get(digest)


def test_changed_content_has_new_address(tmp_path: Path):
    archive = ContentAddressedArchive(tmp_path / "cas")
    first = archive.put(b"original")
    second = archive.put(b"changed")
    assert first != second
    assert archive.get(first) == b"original"
    assert archive.get(second) == b"changed"


def test_reference_is_immutable():
    ref = HistoricalEvidenceReference("EXP-004", "a" * 64)
    with pytest.raises((AttributeError, TypeError)):
        ref.content_hash = "b" * 64
