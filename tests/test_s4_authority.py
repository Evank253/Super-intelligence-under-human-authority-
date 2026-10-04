from datetime import datetime, timezone
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from s4_authority.authorization import AuthorizationPayload
from s4_authority.canonical import digest
from s4_authority.verifier import verify_authorization
import s4_authority

NOW = datetime(2026, 10, 4, 8, 0, tzinfo=timezone.utc)

def payload(**kw):
    base = dict(version="1", authority_id="ext-1", action="execute", subject="KCN-N1", scope=("benchmark:ASI-S4",), valid_from="2026-10-04T00:00:00+00:00", valid_until="2026-10-05T00:00:00+00:00", policy_version="CEP-001", transition_id="transition-1")
    base.update(kw)
    return AuthorizationPayload(**base)

def external_sign(p):
    key = Ed25519PrivateKey.generate()
    sig = key.sign(digest(p.as_dict()))
    return key.public_key(), sig

def test_package_exposes_no_signing_primitive():
    assert not hasattr(s4_authority, "sign")
    assert not any(name.startswith("sign") for name in dir(s4_authority))

def test_signature_without_witness_is_not_measured():
    p = payload()
    pub, sig = external_sign(p)
    v = verify_authorization(p, sig, pub, {}, now=NOW, requested_scope=p.scope)
    assert v.status == "NOT_MEASURED" and v.effective_authority == "NONE"

def test_external_signature_and_witness_is_candidate_not_grant():
    p = payload()
    pub, sig = external_sign(p)
    v = verify_authorization(p, sig, pub, {digest(p.as_dict()): sig}, now=NOW, requested_scope=p.scope)
    assert v.status == "AUTHORIZATION_CANDIDATE" and v.effective_authority == "NONE"

def test_scope_reorder_has_one_digest():
    a = payload(scope=("B", "A"))
    b = payload(scope=("A", "B"))
    assert digest(a.as_dict()) == digest(b.as_dict())

def test_scope_expansion_rejected():
    p = payload(scope=("A",))
    pub, sig = external_sign(p)
    v = verify_authorization(p, sig, pub, {digest(p.as_dict()): sig}, now=NOW, requested_scope=("A", "B"))
    assert v.status == "INVALID"

def test_replay_changed_transition_rejected():
    p = payload()
    pub, sig = external_sign(p)
    other = payload(transition_id="transition-2")
    v = verify_authorization(other, sig, pub, {digest(p.as_dict()): sig}, now=NOW, requested_scope=other.scope)
    assert v.status == "INVALID"

def test_stale_rejected():
    p = payload(valid_until="2026-10-04T01:00:00+00:00")
    pub, sig = external_sign(p)
    later = datetime(2026, 10, 4, 8, 0, tzinfo=timezone.utc)
    v = verify_authorization(p, sig, pub, {digest(p.as_dict()): sig}, now=later, requested_scope=p.scope)
    assert v.status == "INVALID"

def test_manufactured_text_rejected():
    p = payload()
    pub, _ = external_sign(p)
    v = verify_authorization(p, b"Evan Ketchum approved this", pub, {}, now=NOW, requested_scope=p.scope)
    assert v.status == "INVALID" and v.effective_authority == "NONE"

def test_forged_witness_rejected():
    p = payload()
    pub, sig = external_sign(p)
    v = verify_authorization(p, sig, pub, {digest(p.as_dict()): b"forged"}, now=NOW, requested_scope=p.scope)
    assert v.status == "INVALID"
