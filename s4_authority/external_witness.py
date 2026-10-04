"""Read-only witness log. This module has no append, set, or replace API."""
import json
from pathlib import Path
from .witness import WitnessRecord

class ReadOnlyWitnessLog:
    def __init__(self, path: str):
        self._path = Path(path)

    def retrieve(self, authorization_id: str):
        if not self._path.is_file():
            return None
        with self._path.open("r", encoding="utf-8") as handle:
            rows = json.load(handle)
        row = rows.get(authorization_id)
        if row is None:
            return None
        signature = bytes.fromhex(row["witness_signature_hex"])
        fields = {k: row[k] for k in ("authorization_id", "digest_hex", "signature_hex", "witnessed_at", "witness_id")}
        return WitnessRecord(**fields), signature
