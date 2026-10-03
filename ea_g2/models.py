"""Immutable EA-G2 evolutionary records.

Historical evidence is represented only by a typed reference. No HistoricalRecord
object is defined or stored in this runtime.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

@dataclass(frozen=True, slots=True)
class Provenance:
    origin: str
    lineage: str
    source: str
    source_hash: str | None = None
    def __post_init__(self):
        for name in ("origin", "lineage", "source"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} is required")

@dataclass(frozen=True, slots=True)
class ChallengeRecord:
    challenge_id: str
    subject_record_id: str
    challenge_state: Literal[
        "RESOLVED_SUPPORTED","RESOLVED_REFUTED","PARTIALLY_RESOLVED",
        "UNRESOLVED","NOT_MEASURED","SUPERSEDED"
    ]
    provenance: Provenance
    def __post_init__(self):
        if not self.challenge_id or not self.subject_record_id:
            raise ValueError("challenge_id and subject_record_id are required")

@dataclass(frozen=True, slots=True)
class EvolutionRecord:
    evolution_id: str
    historical_record_id: str
    historical_hash: str
    prior_interpretation: str
    new_evidence: tuple[str, ...]
    new_interpretation: str
    reason_for_change: str
    change_classification: Literal["CORRECTION","REFINEMENT","EXTENSION","REINTERPRETATION"]
    historical_record_preserved: bool
    historical_impact: Literal["NONE"]
    provenance: Provenance
    human_ratification_id: str | None = None
    def __post_init__(self):
        if not self.evolution_id or not self.historical_record_id:
            raise ValueError("evolution_id and historical_record_id are required")
        if len(self.historical_hash) != 64:
            raise ValueError("historical_hash must be a SHA-256 digest")
        try: int(self.historical_hash, 16)
        except ValueError as exc: raise ValueError("historical_hash must be hexadecimal") from exc
        if not self.historical_record_preserved or self.historical_impact != "NONE":
            raise ValueError("EA-G2 evolution cannot claim historical mutation")
        if not self.new_evidence:
            raise ValueError("new_evidence is required")

@dataclass(frozen=True, slots=True)
class HumanRatificationRecord:
    ratification_id: str
    subject_record_id: str
    decision: Literal["RATIFIED","REJECTED","RATIFIED_WITH_CONDITIONS"]
    scope: str
    conditions: tuple[str, ...]
    rationale: str
    provenance: Provenance
    def __post_init__(self):
        if not self.ratification_id or not self.subject_record_id:
            raise ValueError("ratification_id and subject_record_id are required")
