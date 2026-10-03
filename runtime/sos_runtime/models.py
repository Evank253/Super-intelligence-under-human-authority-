from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import uuid

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def new_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex}"

@dataclass
class ArtifactRecord:
    artifact_id: str
    artifact_type: str
    name: str
    source_system: str
    source_repository: Optional[str]
    source_commit: Optional[str]
    source_tree_hash: Optional[str]
    source_path: Optional[str]
    created_at: str
    observed_at: str
    parent_artifact_id: Optional[str] = None
    construction_method: Optional[str] = None
    capabilities: List[str] = field(default_factory=list)
    status: str = "DISCOVERED"
    evidence_state: str = "NOT_MEASURED"
    verification_state: str = "NOT_MEASURED"
    qualification_state: str = "NOT_MEASURED"
    adoption_state: str = "NOT_AUTHORIZED"
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class AuthorizationRecord:
    authorization_id: str
    action: str
    subject: str
    authority_source: str
    constitutional_basis: str
    scope: List[str]
    delegated_by: Optional[str]
    issued_at: str
    expires_at: Optional[str]
    revocation_status: str = "ACTIVE"
    human_ratification: str = "NOT_MEASURED"
    status: str = "ACTIVE"

@dataclass
class EvidenceRecord:
    evidence_id: str
    subject_id: str
    evidence_type: str
    source: str
    observed_at: str
    artifact_hash: Optional[str]
    disposition: str = "OBSERVED"
    scope: str = "UNSCOPED"
