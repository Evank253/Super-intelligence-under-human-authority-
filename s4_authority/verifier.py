from dataclasses import dataclass
from datetime import datetime
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from .canonical import digest
from .witness import witness_digest

@dataclass(frozen=True, slots=True)
class AuthorizationVerdict:
    status: str
    effective_authority: str
    reason: str

def verify_authorization(payload, signature: bytes, authorization_public_key: Ed25519PublicKey, witness_log, witness_public_key: Ed25519PublicKey, *, now: datetime, requested_scope: tuple[str, ...]):
    """Derive a verdict. The caller cannot supply the witness record."""
    try:
        payload_digest = digest(payload.as_dict())
        authorization_public_key.verify(signature, payload_digest)
    except (InvalidSignature, ValueError, TypeError):
        return AuthorizationVerdict("INVALID", "NONE", "Authorization signature does not match the canonical digest.")
    found = witness_log.retrieve(payload.authority_id)
    if found is None:
        return AuthorizationVerdict("NOT_MEASURED", "NONE", "External witness entry is absent.")
    record, witness_signature = found
    if record.digest_hex != payload_digest.hex() or record.signature_hex != signature.hex():
        return AuthorizationVerdict("INVALID", "NONE", "Witness binding does not match the signed authorization.")
    try:
        witness_public_key.verify(witness_signature, witness_digest(record))
    except (InvalidSignature, ValueError, TypeError):
        return AuthorizationVerdict("INVALID", "NONE", "Witness signature was not produced by the pinned witness key.")
    if not set(requested_scope).issubset(set(payload.scope)):
        return AuthorizationVerdict("INVALID", "NONE", "Requested scope exceeds the signed scope.")
    start = datetime.fromisoformat(payload.valid_from)
    end = datetime.fromisoformat(payload.valid_until)
    if now < start or now > end:
        return AuthorizationVerdict("INVALID", "NONE", "Signed authorization is stale or not yet valid.")
    return AuthorizationVerdict("AUTHORIZATION_CANDIDATE", "NONE", "External authorization and witness signatures match. This is not a sovereignty grant.")
