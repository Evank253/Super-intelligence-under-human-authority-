"""Content-addressed historical evidence references for EA-G2."""
from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Literal

_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_SECONDARY_TYPES = {"ipfs-cid", "git-object", "other-content-address"}

@dataclass(frozen=True, slots=True)
class SecondaryIdentifier:
    identifier_type: Literal["ipfs-cid","git-object","other-content-address"]
    content_identifier: str
    hash_algorithm: str
    representation: str
    role: Literal["secondary"]
    verification_method: str
    verified_against_primary: bool
    verified_at: str
    derivation: str | None = None
    retrieval_reference: str | None = None
    def __post_init__(self):
        if self.identifier_type not in _SECONDARY_TYPES or not self.content_identifier.strip():
            raise ValueError("invalid secondary identifier")
        if self.role != "secondary" or not self.hash_algorithm.strip() or not self.representation.strip():
            raise ValueError("invalid secondary metadata")
        if not self.verification_method.strip() or not self.verified_at.strip() or self.verified_against_primary is not True:
            raise ValueError("secondary identifier must have explicit primary verification")

@dataclass(frozen=True, slots=True)
class PrimaryIdentity:
    identifier_type: Literal["sha256-raw"]
    content_identifier: str
    hash_algorithm: Literal["SHA-256"]
    representation: Literal["raw-bytes"]
    role: Literal["primary"]
    def __post_init__(self):
        if self.identifier_type != "sha256-raw" or self.hash_algorithm != "SHA-256" or self.representation != "raw-bytes" or self.role != "primary":
            raise ValueError("primary identity must be SHA-256 over raw bytes")
        if not _HEX64.fullmatch(self.content_identifier):
            raise ValueError("primary content_identifier must be 64 lowercase hex characters")

@dataclass(frozen=True, slots=True)
class HistoricalEvidenceReference:
    record_id: str
    primary_identity: PrimaryIdentity
    secondary_identifiers: tuple[SecondaryIdentifier, ...] = ()
    provenance: object | None = None
    def __post_init__(self):
        if not self.record_id.strip():
            raise ValueError("record_id is required")
        if not isinstance(self.primary_identity, PrimaryIdentity):
            raise TypeError("primary_identity is required")
        seen=set()
        for item in self.secondary_identifiers:
            key=(item.identifier_type,item.content_identifier)
            if key in seen: raise ValueError("duplicate secondary identifier")
            seen.add(key)
    @property
    def content_hash(self): return self.primary_identity.content_identifier
    @property
    def hash_algorithm(self): return self.primary_identity.hash_algorithm
