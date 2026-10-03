"""Immutable references from evolutionary state to historical evidence."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HistoricalEvidenceReference:
    record_id: str
    content_hash: str
    hash_algorithm: str = "SHA-256"

    def __post_init__(self) -> None:
        if not self.record_id:
            raise ValueError("record_id is required")
        if self.hash_algorithm != "SHA-256":
            raise ValueError("EA-G2 initially requires SHA-256")
        if len(self.content_hash) != 64:
            raise ValueError("content_hash must be a SHA-256 digest")
        try:
            int(self.content_hash, 16)
        except ValueError as exc:
            raise ValueError("content_hash must be hexadecimal") from exc
