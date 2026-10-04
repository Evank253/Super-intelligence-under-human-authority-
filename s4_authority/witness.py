import hashlib, json
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WitnessRecord:
    authorization_id: str
    digest_hex: str
    signature_hex: str
    witnessed_at: str
    witness_id: str

    def canonical(self) -> bytes:
        body = {
            "authorization_id": self.authorization_id,
            "digest_hex": self.digest_hex,
            "signature_hex": self.signature_hex,
            "witnessed_at": self.witnessed_at,
            "witness_id": self.witness_id,
        }
        return json.dumps(body, separators=(",", ":"), sort_keys=True).encode("utf-8")

def witness_digest(record: WitnessRecord) -> bytes:
    return hashlib.sha256(record.canonical()).digest()
