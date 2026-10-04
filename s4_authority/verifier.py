from dataclasses import dataclass
from datetime import datetime
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from .canonical import digest

@dataclass(frozen=True, slots=True)
class AuthorizationVerdict:
    status: str
    effective_authority: str
    reason: str

def verify_authorization(payload, signature: bytes, public_key: Ed25519PublicKey, witness: dict, *, now: datetime, requested_scope: tuple[str, ...]):
    """Derive a verdict. No caller-supplied result is accepted."""
    try:
        payload_digest = digest(payload.as_dict())
        public_key.verify(signature, payload_digest)
    except (InvalidSignature, ValueError, TypeError):
        return AuthorizationVerdict("INVALID", "NONE", "Signature does not match the canonical digest.")
    witnessed = witness.get(payload_digest)
    if witnessed is None:
        return AuthorizationVerdict("NOT_MEASURED", "NONE", "Signature verified but external witness entry is absent.")
    if witnessed != signature:
        return AuthorizationVerdict("INVALID", "NONE", "Witness entry does not match the signature.")
    if not set(requested_scope).issubset(set(payload.scope)):
        return AuthorizationVerdict("INVALID", "NONE", "Requested scope exceeds the signed scope.")
    start = datetime.fromisoformat(payload.valid_from)
    end = datetime.fromisoformat(payload.valid_until)
    if now < start or now > end:
        return AuthorizationVerdict("INVALID", "NONE", "Signed authorization is stale or not yet valid.")
    return AuthorizationVerdict("AUTHORIZATION_CANDIDATE", "NONE", "External signature and witness match. This is not a sovereignty grant.")
