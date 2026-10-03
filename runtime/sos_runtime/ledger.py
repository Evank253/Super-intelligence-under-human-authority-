import hashlib, json
from pathlib import Path

class AppendOnlyLedger:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)

    def append(self, event):
        raw = json.dumps(event, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256(raw.encode()).hexdigest()
        record = dict(event)
        record["record_hash"] = digest
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, sort_keys=True) + "\n")
        return digest

    def read(self):
        return [json.loads(x) for x in self.path.read_text(encoding="utf-8").splitlines() if x.strip()]

    def verify(self):
        rows = self.read()
        valid = True
        for row in rows:
            supplied = row.pop("record_hash", None)
            raw = json.dumps(row, sort_keys=True, separators=(",", ":"))
            valid = valid and supplied == hashlib.sha256(raw.encode()).hexdigest()
            row["record_hash"] = supplied
        return {"valid": valid, "records": len(rows)}
