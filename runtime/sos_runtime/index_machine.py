from dataclasses import asdict
from .models import ArtifactRecord, new_id, now_iso

class IndexMachine:
    """Provenance/temporal witness. It records occurrence; it never grants authority."""
    def __init__(self, ledger):
        self.ledger = ledger
        self.artifacts = {}

    def register(self, artifact_type, name, source_system, source_repository=None,
                 source_commit=None, source_tree_hash=None, source_path=None,
                 parent_artifact_id=None, construction_method=None,
                 capabilities=None, metadata=None):
        t = now_iso()
        rec = ArtifactRecord(
            new_id("artifact"), artifact_type, name, source_system,
            source_repository, source_commit, source_tree_hash, source_path,
            t, t, parent_artifact_id, construction_method,
            capabilities or [], metadata=metadata or {})
        self.artifacts[rec.artifact_id] = rec
        self.ledger.append({"kind":"INDEX_REGISTER","timestamp":t,"artifact":asdict(rec)})
        return rec

    def reindex(self, artifact_id, changes):
        old = self.artifacts[artifact_id]
        data = asdict(old)
        data.update(changes)
        data["artifact_id"] = new_id("artifact")
        data["parent_artifact_id"] = old.artifact_id
        data["observed_at"] = now_iso()
        rec = ArtifactRecord(**data)
        self.artifacts[rec.artifact_id] = rec
        self.ledger.append({"kind":"INDEX_REINDEX","timestamp":rec.observed_at,
                            "previous_artifact_id":old.artifact_id,"artifact":asdict(rec)})
        return rec

    def lineage(self, artifact_id):
        chain = []
        cur = self.artifacts.get(artifact_id)
        while cur:
            chain.append(cur)
            cur = self.artifacts.get(cur.parent_artifact_id) if cur.parent_artifact_id else None
        return list(reversed(chain))
