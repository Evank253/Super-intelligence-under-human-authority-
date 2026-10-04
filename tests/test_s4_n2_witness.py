import json
from datetime import datetime, timezone
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from s4_authority.authorization import AuthorizationPayload
from s4_authority.canonical import digest
from s4_authority.external_witness import ReadOnlyWitnessLog
from s4_authority.verifier import verify_authorization
from s4_authority.witness import WitnessRecord, witness_digest
import s4_authority, s4_authority.external_witness as ew

NOW = datetime(2026, 10, 4, 8, 0, tzinfo=timezone.utc)

def payload():
    return AuthorizationPayload("1", "ext-1", "execute", "KCN-N1", ("benchmark:ASI-S4",), "2026-10-04T00:00:00+00:00", "2026-10-05T00:00:00+00:00", "CEP-001", "transition-1")

def test_no_write_or_sign_api():
    banned = {"sign", "append_witness", "set_witness", "replace_witness", "register_witness"}
    assert banned.isdisjoint(set(dir(s4_authority)) | set(dir(ew)) | set(dir(ReadOnlyWitnessLog)))

def test_s1_s3_forged_log_rejected(tmp_path: Path):
    p = payload()
    auth_key = Ed25519PrivateKey.generate()
    sig = auth_key.sign(digest(p.as_dict()))
    witness_key = Ed25519PrivateKey.generate()
    forged = WitnessRecord(p.authority_id, digest(p.as_dict()).hex(), sig.hex(), NOW.isoformat(), "forged")
    row = {"authorization_id": forged.authorization_id, "digest_hex": forged.digest_hex, "signature_hex": forged.signature_hex, "witnessed_at": forged.witnessed_at, "witness_id": forged.witness_id, "witness_signature_hex": b"not-a-witness-signature".hex()}
    path = tmp_path / "witness.json"
    path.write_text(json.dumps({p.authority_id: row}))
    v = verify_authorization(p, sig, auth_key.public_key(), ReadOnlyWitnessLog(path), witness_key.public_key(), now=NOW, requested_scope=p.scope)
    assert v.status == "INVALID" and v.effective_authority == "NONE"

def test_missing_witness_not_measured(tmp_path: Path):
    p = payload()
    auth_key = Ed25519PrivateKey.generate()
    sig = auth_key.sign(digest(p.as_dict()))
    witness_key = Ed25519PrivateKey.generate()
    path = tmp_path / "missing.json"
    v = verify_authorization(p, sig, auth_key.public_key(), ReadOnlyWitnessLog(path), witness_key.public_key(), now=NOW, requested_scope=p.scope)
    assert v.status == "NOT_MEASURED" and v.effective_authority == "NONE"

def test_external_witness_is_candidate_not_grant(tmp_path: Path):
    p = payload()
    auth_key = Ed25519PrivateKey.generate()
    sig = auth_key.sign(digest(p.as_dict()))
    witness_key = Ed25519PrivateKey.generate()
    record = WitnessRecord(p.authority_id, digest(p.as_dict()).hex(), sig.hex(), NOW.isoformat(), "witness-1")
    wsig = witness_key.sign(witness_digest(record))
    row = {"authorization_id": record.authorization_id, "digest_hex": record.digest_hex, "signature_hex": record.signature_hex, "witnessed_at": record.witnessed_at, "witness_id": record.witness_id, "witness_signature_hex": wsig.hex()}
    path = tmp_path / "witness.json"
    path.write_text(json.dumps({p.authority_id: row}))
    v = verify_authorization(p, sig, auth_key.public_key(), ReadOnlyWitnessLog(path), witness_key.public_key(), now=NOW, requested_scope=p.scope)
    assert v.status == "AUTHORIZATION_CANDIDATE" and v.effective_authority == "NONE"
