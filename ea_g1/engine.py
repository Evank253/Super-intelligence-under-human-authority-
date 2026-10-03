from copy import deepcopy
from dataclasses import asdict
from typing import Any, Dict
from .models import BottleneckRecord, ChallengeRecord, EvolutionRecord, HumanRatificationRecord, HistoricalRecord, canonical_hash

ALLOWED_CHANGE_CLASSIFICATIONS = {"ARCHITECTURAL", "INTERPRETIVE", "IMPLEMENTATION", "EVIDENCE_STATUS", "GOVERNANCE"}

class GovernanceViolation(Exception): pass
class HistoricalMutationError(GovernanceViolation): pass
class AuthorityBoundaryError(GovernanceViolation): pass
class ProvenanceError(GovernanceViolation): pass
class EvolutionTraceabilityError(GovernanceViolation): pass

class EAG1Store:
    def __init__(self):
        self.historical: Dict[str, HistoricalRecord] = {}
        self.challenges: Dict[str, ChallengeRecord] = {}
        self.bottlenecks: Dict[str, BottleneckRecord] = {}
        self.evolutions: Dict[str, EvolutionRecord] = {}
        self.ratifications: Dict[str, HumanRatificationRecord] = {}
        self.authority_boundary = "EXTERNAL_HUMAN"

    @staticmethod
    def _require_provenance(record: Any) -> None:
        p = getattr(record, "provenance", None)
        if not p or not p.origin or not p.source or not p.lineage:
            raise ProvenanceError("origin, source, and non-empty lineage are required")

    def add_historical(self, record: HistoricalRecord) -> None:
        self._require_provenance(record)
        if record.record_id in self.historical:
            raise HistoricalMutationError("historical record already exists and is frozen")
        self.historical[record.record_id] = deepcopy(record)

    def get_historical(self, record_id: str) -> Dict[str, Any]:
        return self.historical[record_id].snapshot()

    def mutate_historical(self, record_id: str, **changes: Any) -> None:
        if record_id not in self.historical: raise KeyError(record_id)
        raise HistoricalMutationError("historical records are immutable")

    def add_challenge(self, record: ChallengeRecord) -> None:
        self._require_provenance(record)
        if record.challenge_id in self.challenges: raise GovernanceViolation("duplicate challenge_id")
        self.challenges[record.challenge_id] = deepcopy(record)

    def authorize_from_challenge(self, challenge_id: str) -> None:
        raise AuthorityBoundaryError("challenge cannot grant authority")

    def authorize_from_evidence(self, evidence_id: str) -> None:
        raise AuthorityBoundaryError("evidence cannot independently grant authority")

    def authorize_from_qualification(self, qualification_id: str) -> None:
        raise AuthorityBoundaryError("qualification cannot independently grant authority")

    def upgrade_from_consensus(self, record_ids: list[str]) -> None:
        raise AuthorityBoundaryError("consensus cannot independently upgrade evidentiary status")

    def create_evolution(self, record: EvolutionRecord) -> None:
        self._require_provenance(record)
        if record.change_classification not in ALLOWED_CHANGE_CLASSIFICATIONS:
            raise EvolutionTraceabilityError("invalid change_classification")
        if not record.predecessor_record:
            raise EvolutionTraceabilityError("predecessor_record is required")
        if not record.historical_record_preserved or record.historical_impact != "NONE":
            raise HistoricalMutationError("EA-G1 evolution must preserve historical records with historical_impact=NONE")
        if record.evolution_id in self.evolutions: raise EvolutionTraceabilityError("duplicate evolution_id")
        self.evolutions[record.evolution_id] = deepcopy(record)

    def modify_architecture_from_inside(self, requested_boundary: str) -> None:
        raise AuthorityBoundaryError("recursive components may propose authority-boundary changes, but cannot authorize them")

    def add_ratification(self, record: HumanRatificationRecord) -> None:
        self._require_provenance(record)
        if record.decision not in {"AUTHORIZED", "REJECTED", "CONDITIONAL", "DEFERRED"}:
            raise GovernanceViolation("invalid human decision")
        if record.ratification_id in self.ratifications: raise GovernanceViolation("duplicate ratification_id")
        self.ratifications[record.ratification_id] = deepcopy(record)

    def verify(self) -> Dict[str, Any]:
        return {"historical_records": len(self.historical), "challenge_records": len(self.challenges),
                "evolution_records": len(self.evolutions), "human_ratifications": len(self.ratifications),
                "authority_boundary": self.authority_boundary, "invariants_enforced_by_mechanism": True}

    def record_hash(self, record: Any) -> str:
        return canonical_hash(asdict(record))
