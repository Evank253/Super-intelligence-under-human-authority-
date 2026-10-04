"""Executable TransitionRecord validation and anti-promotion boundary.

This module does not mint sovereign authorization. An in-process verifier,
string attestation, or caller-supplied result cannot establish S4 authority.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Callable, FrozenSet, Mapping, Optional

class TransitionClass(str, Enum):
    EPISTEMIC="EPISTEMIC"; CAPABILITY="CAPABILITY"; QUALIFICATION="QUALIFICATION"
    GOVERNANCE="GOVERNANCE"; AUTHORITY="AUTHORITY"; AUTONOMY="AUTONOMY"

class DecisionOrigin(str, Enum):
    S1="S1"; S2="S2"; S3="S3"; S4="S4"; SYSTEM="SYSTEM"; EXTERNAL_HUMAN="EXTERNAL_HUMAN"

class AuthorityOrigin(str, Enum):
    NONE="NONE"; S1="S1"; S2="S2"; S3="S3"; SYSTEM="SYSTEM"; S4_EXTERNAL_HUMAN="S4_EXTERNAL_HUMAN"

class ValidationStatus(str, Enum):
    VALID="VALID"; INVALID="INVALID"; NOT_MEASURED="NOT_MEASURED"
    UNRESOLVED="UNRESOLVED"; AUTHORIZATION_REQUIRED="AUTHORIZATION_REQUIRED"

@dataclass(frozen=True, slots=True)
class S4AuthorizationRecord:
    authority_id: str
    action: str
    subject: str
    scope: FrozenSet[str]
    issued_at: datetime
    valid_from: datetime
    valid_until: Optional[datetime]
    external_attestation: str
    origin: AuthorityOrigin = AuthorityOrigin.S4_EXTERNAL_HUMAN

@dataclass(frozen=True, slots=True)
class TransitionRecord:
    transition_id: str
    transition_class: TransitionClass
    source_state: str
    destination_state: str
    subject: str
    scope: FrozenSet[str]
    timestamp: datetime
    preconditions: FrozenSet[str]
    evidence_refs: tuple[str, ...]
    verification_refs: tuple[str, ...]
    qualification_refs: tuple[str, ...]
    governance_refs: tuple[str, ...]
    authority_ref: Optional[str]
    provenance: tuple[str, ...]
    decision_actor: str
    decision_origin: DecisionOrigin
    temporal_validity: tuple[datetime, Optional[datetime]]
    result: ValidationStatus
    failure_reason: Optional[str] = None

@dataclass(frozen=True, slots=True)
class ValidationResult:
    status: ValidationStatus
    effective_authority: str
    reason: str

S4_STATES=frozenset({"S4_AUTHORIZATION","AUTHORIZED"})
S4_SOURCE_FOR={"S4_AUTHORIZATION":frozenset({"GOVERNED"}),"AUTHORIZED":frozenset({"GOVERNED","S4_AUTHORIZATION"})}
LOWER_ORIGINS=frozenset({DecisionOrigin.S1,DecisionOrigin.S2,DecisionOrigin.S3,DecisionOrigin.SYSTEM})
PROMOTION_PAIRS=frozenset({
    ("NOT_MEASURED","QUALIFIED"),("NOT_MEASURED","AUTHORIZED"),("NOT_MEASURED","GOVERNED"),
    ("UNRESOLVED","AUTHORIZED"),("UNKNOWN","AUTHORIZED"),("CAPABILITY","AUTHORITY"),
    ("EVIDENCE","SOVEREIGNTY"),("EVIDENCE","AUTHORIZED"),("QUALIFICATION","SOVEREIGNTY"),
    ("QUALIFIED","AUTHORIZED"),("DELEGATION","SOVEREIGNTY"),("S3_RECOMMENDATION","S4_AUTHORIZATION"),
    ("SYSTEM_GENERATED","HUMAN_SOVEREIGN_ACT"),
})

def _within_scope(requested, authorized):
    return requested.issubset(authorized)

def _time_valid(at, interval):
    start,end=interval
    return at >= start and (end is None or at <= end)

class TransitionValidator:
    """Validate transitions without trusting destination labels or caller results."""
    def __init__(self, authority_records: Mapping[str,S4AuthorizationRecord]|None=None,
                 external_authority_verifier: Callable[[S4AuthorizationRecord],bool]|None=None):
        self._authority_records=dict(authority_records or {})
        self._external_authority_verifier=external_authority_verifier

    def validate(self, transition: TransitionRecord, *, now=None, prior_transition=None):
        if not transition.provenance:
            return ValidationResult(ValidationStatus.INVALID,"NONE","Missing transition provenance.")
        if not _time_valid(transition.timestamp,transition.temporal_validity):
            return ValidationResult(ValidationStatus.INVALID,"NONE","Transition timestamp is outside its validity interval.")
        if now is not None and not _time_valid(now,transition.temporal_validity):
            return ValidationResult(ValidationStatus.INVALID,"NONE","Transition is not temporally valid now.")
        if (transition.source_state,transition.destination_state) in PROMOTION_PAIRS:
            return ValidationResult(ValidationStatus.INVALID,"NONE","Forbidden anti-promotion transition.")
        if transition.destination_state in S4_STATES:
            return self._validate_s4(transition,now,prior_transition)
        if transition.transition_class == TransitionClass.AUTHORITY:
            return ValidationResult(ValidationStatus.INVALID,"NONE","Authority transitions require externally validated S4 authorization.")
        if transition.destination_state=="QUALIFIED" and not transition.qualification_refs:
            return ValidationResult(ValidationStatus.NOT_MEASURED,"NONE","Qualification evidence is absent.")
        if transition.destination_state=="GOVERNED" and not transition.governance_refs:
            return ValidationResult(ValidationStatus.NOT_MEASURED,"NONE","Governance evidence is absent.")
        return ValidationResult(ValidationStatus.VALID,"NONE","Transition requirements satisfied. Caller result was not consulted.")

    def _validate_s4(self, transition, now, prior_transition):
        allowed=S4_SOURCE_FOR.get(transition.destination_state, frozenset())
        if transition.source_state not in allowed:
            return ValidationResult(ValidationStatus.INVALID,"NONE","S4 destination is not reachable from this source state.")
        if transition.decision_origin in LOWER_ORIGINS:
            return ValidationResult(ValidationStatus.AUTHORIZATION_REQUIRED,"NONE","S1-S3 or system origin cannot produce S4 authority.")
        if transition.authority_ref is None:
            return ValidationResult(ValidationStatus.AUTHORIZATION_REQUIRED,"NONE","No sovereign authority reference supplied.")
        record=self._authority_records.get(transition.authority_ref)
        if record is None:
            return ValidationResult(ValidationStatus.AUTHORIZATION_REQUIRED,"NONE","Sovereign authority record is absent.")
        if record.origin != AuthorityOrigin.S4_EXTERNAL_HUMAN:
            return ValidationResult(ValidationStatus.INVALID,"NONE","Authority origin is not external human S4.")
        if record.subject != transition.subject:
            return ValidationResult(ValidationStatus.INVALID,"NONE","S4 subject mismatch.")
        if not _within_scope(transition.scope,record.scope):
            return ValidationResult(ValidationStatus.INVALID,"NONE","S4 scope does not cover requested scope.")
        if prior_transition is not None and not _within_scope(transition.scope,prior_transition.scope):
            return ValidationResult(ValidationStatus.INVALID,"NONE","Authorization scope expanded without a new S4 authorization.")
        if not _time_valid(transition.timestamp,(record.valid_from,record.valid_until)):
            return ValidationResult(ValidationStatus.INVALID,"NONE","S4 authorization is not temporally valid.")
        if now is not None and not _time_valid(now,(record.valid_from,record.valid_until)):
            return ValidationResult(ValidationStatus.INVALID,"NONE","S4 authorization is stale or expired.")
        if not transition.provenance or transition.provenance[-1] != transition.authority_ref:
            return ValidationResult(ValidationStatus.INVALID,"NONE","Provenance does not terminate at cited S4 authority record.")
        return ValidationResult(ValidationStatus.NOT_MEASURED,"NONE","In-process attestation cannot establish an external sovereign act.")

def effective_authority(transition, validation):
    return "NONE"
