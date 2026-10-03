from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import hashlib, json

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def canonical_hash(value: Dict[str, Any]) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()

@dataclass(frozen=True)
class Provenance:
    origin: str
    lineage: List[str]
    source: str
    source_hash: Optional[str] = None

@dataclass
class ChallengeRecord:
    challenge_id: str
    origin_system: str
    target_system: str
    claim: str
    challenge: str
    challenge_basis: str
    provenance: Provenance
    evidence_requested: List[str] = field(default_factory=list)
    evidence_supplied: List[str] = field(default_factory=list)
    counterclaim: Optional[str] = None
    counterevidence: List[str] = field(default_factory=list)
    verification_state: str = "NOT_MEASURED"
    qualification_state: str = "NOT_MEASURED"
    resolution_state: str = "UNRESOLVED"
    resolution_basis: Optional[str] = None
    human_ratification_id: Optional[str] = None
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)

@dataclass
class BottleneckRecord:
    bottleneck_id: str
    observed_constraint: str
    affected_system: str
    decomposition: List[str]
    baseline: Dict[str, Any]
    proposed_intervention: str
    provenance: Provenance
    implementation: Optional[Dict[str, Any]] = None
    measurement: Optional[Dict[str, Any]] = None
    outcome: Optional[Dict[str, Any]] = None
    challenges: List[str] = field(default_factory=list)
    verification: str = "NOT_MEASURED"
    qualification: str = "NOT_MEASURED"
    human_ratification_id: Optional[str] = None
    next_action: Optional[str] = None

@dataclass
class EvolutionRecord:
    evolution_id: str
    predecessor_record: str
    triggering_evidence: List[str]
    prior_interpretation: str
    new_interpretation: str
    reason_for_change: str
    change_classification: str
    historical_record_preserved: bool
    provenance: Provenance
    verification_state: str = "NOT_MEASURED"
    qualification_state: str = "NOT_MEASURED"
    human_ratification_id: Optional[str] = None
    historical_impact: str = "NONE"
    created_at: str = field(default_factory=now_iso)

@dataclass
class HumanRatificationRecord:
    ratification_id: str
    human_authority: str
    subject_record: str
    decision: str
    scope: str
    conditions: List[str]
    rationale: str
    provenance: Provenance
    timestamp: str = field(default_factory=now_iso)

@dataclass
class HistoricalRecord:
    record_id: str
    status: str
    payload: Dict[str, Any]
    provenance: Provenance
    frozen: bool = True
    def snapshot(self) -> Dict[str, Any]:
        return asdict(self)
