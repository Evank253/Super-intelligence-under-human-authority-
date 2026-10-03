"""EA-G2 governed evolutionary state.

This runtime deliberately owns no historical evidence objects. It stores only
immutable references (record ID + SHA-256 identity) and interpretive records.
"""

from __future__ import annotations
from dataclasses import replace
from types import MappingProxyType
from typing import Mapping

from evidence_archive import ContentAddressedArchive, HistoricalEvidenceReference, IntegrityError
from .models import ChallengeRecord, EvolutionRecord, HumanRatificationRecord, Provenance

class AuthorityBoundaryError(PermissionError): pass
class HistoricalReferenceError(ValueError): pass
class ProvenanceError(ValueError): pass

class EvolutionaryState:
    __slots__ = ("_archive", "_challenges", "_evolutions", "_ratifications", "__initialized")
    AUTHORITY_BOUNDARY = "EXTERNAL_HUMAN"

    def __init__(self, archive: ContentAddressedArchive):
        object.__setattr__(self, "_archive", archive)
        object.__setattr__(self, "_challenges", {})
        object.__setattr__(self, "_evolutions", {})
        object.__setattr__(self, "_ratifications", {})
        object.__setattr__(self, "_EvolutionaryState__initialized", True)

    @property
    def authority_boundary(self) -> str:
        return type(self).AUTHORITY_BOUNDARY

    @property
    def challenges(self) -> Mapping[str, ChallengeRecord]:
        return MappingProxyType(dict(self._challenges))

    @property
    def evolutions(self) -> Mapping[str, EvolutionRecord]:
        return MappingProxyType(dict(self._evolutions))

    @property
    def ratifications(self) -> Mapping[str, HumanRatificationRecord]:
        return MappingProxyType(dict(self._ratifications))

    def _check_provenance(self, p: Provenance):
        if not isinstance(p, Provenance):
            raise ProvenanceError("valid Provenance is required")

    def add_challenge(self, record: ChallengeRecord) -> None:
        self._check_provenance(record.provenance)
        if record.challenge_id in self._challenges: raise ValueError("duplicate challenge_id")
        self._challenges = {**self._challenges, record.challenge_id: record}

    def add_evolution(self, record: EvolutionRecord) -> None:
        self._check_provenance(record.provenance)
        if record.evolution_id in self._evolutions: raise ValueError("duplicate evolution_id")
        ref = HistoricalEvidenceReference(record.historical_record_id, record.historical_hash)
        if not self._archive.has(ref.content_hash):
            raise HistoricalReferenceError("historical reference is not present and verifiable in archive")
        if record.historical_record_id.startswith("HIST-") and not record.historical_record_id:
            raise HistoricalReferenceError("invalid historical reference")
        self._evolutions = {**self._evolutions, record.evolution_id: record}

    def add_ratification(self, record: HumanRatificationRecord) -> None:
        self._check_provenance(record.provenance)
        if record.ratification_id in self._ratifications: raise ValueError("duplicate ratification_id")
        self._ratifications = {**self._ratifications, record.ratification_id: record}

    def retrieve_verified(self, reference: HistoricalEvidenceReference) -> bytes:
        data = self._archive.get(reference.content_hash)
        if reference.hash_algorithm != "SHA-256":
            raise HistoricalReferenceError("unsupported primary hash algorithm")
        return data

    def authorize_from_challenge(self, *_args, **_kwargs):
        raise AuthorityBoundaryError("challenge cannot create authority")

    def authorize_from_evidence(self, *_args, **_kwargs):
        raise AuthorityBoundaryError("evidence cannot create authority")

    def authorize_from_qualification(self, *_args, **_kwargs):
        raise AuthorityBoundaryError("qualification cannot create authority")

    def upgrade_from_consensus(self, *_args, **_kwargs):
        raise AuthorityBoundaryError("consensus cannot create truth or authority")

    def modify_historical(self, *_args, **_kwargs):
        raise AuthorityBoundaryError("evolutionary runtime has no historical write capability")

    def modify_architecture_from_inside(self, *_args, **_kwargs):
        raise AuthorityBoundaryError("internal state cannot acquire authority")

    def verify(self) -> dict[str, object]:
        return {
            "historical_state_owned": False,
            "authority_boundary": self.authority_boundary,
            "primary_verification_required": True,
            "invariants_enforced_by_public_mechanism": True,
        }

    def __setattr__(self, name, value):
        if getattr(self, "_EvolutionaryState__initialized", False):
            if name in {"_archive","_challenges","_evolutions","_ratifications"}:
                raise AttributeError(f"{name} is runtime-owned state and cannot be directly reassigned")
        object.__setattr__(self, name, value)
