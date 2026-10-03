"""Minimal SHA-256 content-addressed historical evidence store for EA-G2.

The archive is intentionally independent of the evolutionary runtime.
This is an implementation experiment, not a production archive.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


class IntegrityError(Exception):
    """Raised when retrieved content does not match its content address."""


class ArchiveWriteError(Exception):
    """Reserved for future archive-level write/retention failures."""


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


class ContentAddressedArchive:
    """Minimal filesystem CAS.

    The evolutionary runtime may use this archive through explicit read/reference
    operations. It must not receive a writable historical object from the archive.
    """

    def __init__(self, root: Path | str):
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)

    def put(self, content: bytes) -> str:
        """Store bytes under their SHA-256 digest and return the digest.

        This operation creates a new content object. Existing content at the same
        digest is not rewritten.
        """
        if not isinstance(content, bytes):
            raise TypeError("content must be bytes")
        digest = _digest(content)
        path = self._path_for(digest)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            if self._verified_read(digest) != content:
                raise IntegrityError("existing CAS object failed verification")
            return digest
        path.write_bytes(content)
        return digest

    def get(self, digest: str) -> bytes:
        """Retrieve and verify bytes by SHA-256 digest."""
        return self._verified_read(digest)

    def has(self, digest: str) -> bool:
        try:
            self._verified_read(digest)
            return True
        except (FileNotFoundError, IntegrityError):
            return False

    def _verified_read(self, digest: str) -> bytes:
        path = self._path_for(digest)
        data = path.read_bytes()
        if _digest(data) != digest:
            raise IntegrityError("CAS hash mismatch")
        return data

    def _path_for(self, digest: str) -> Path:
        if not isinstance(digest, str) or len(digest) != 64:
            raise ValueError("digest must be a 64-character SHA-256 hex digest")
        try:
            int(digest, 16)
        except ValueError as exc:
            raise ValueError("digest must be hexadecimal") from exc
        return self._root / digest[:2] / digest
