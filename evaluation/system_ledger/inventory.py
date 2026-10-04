"""Filesystem inventory and file-level provenance helpers."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from typing import Iterable

IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache"}

def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        while chunk := fh.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()

def inventory_tree(root: str | Path) -> list[dict]:
    root = Path(root).resolve()
    rows = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in IGNORED_DIRS for part in path.parts):
            continue
        stat = path.stat()
        rows.append({
            "relative_path": path.relative_to(root).as_posix(),
            "size_bytes": stat.st_size,
            "sha256": sha256_file(path),
        })
    return rows

def write_manifest(root: str | Path, output: str | Path) -> dict:
    root = Path(root).resolve()
    manifest = {
        "schema_version": "1.0",
        "root": str(root),
        "files": inventory_tree(root),
    }
    Path(output).write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest

def reconcile_manifests(expected: Iterable[dict], observed: Iterable[dict]) -> dict:
    exp = {row["relative_path"]: row for row in expected}
    obs = {row["relative_path"]: row for row in observed}
    findings = []
    for path in sorted(set(exp) | set(obs)):
        if path not in obs:
            findings.append({"path": path, "status": "MISSING"})
        elif path not in exp:
            findings.append({"path": path, "status": "UNEXPECTED"})
        elif exp[path].get("sha256") != obs[path].get("sha256"):
            findings.append({
                "path": path,
                "status": "HASH_CONFLICT",
                "expected_sha256": exp[path].get("sha256"),
                "observed_sha256": obs[path].get("sha256"),
            })
        else:
            findings.append({"path": path, "status": "AGREEMENT"})
    counts = {}
    for row in findings:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    return {"counts": dict(sorted(counts.items())), "findings": findings}
