"""KSI-ASI transition and authorization gates.

This implementation is intentionally small: it establishes the machine-enforced
boundary before larger legacy components are imported.
"""

from dataclasses import dataclass
from typing import FrozenSet


EVIDENCE_STATES: FrozenSet[str] = frozenset({"E0","E1","E2","E3","E4","E5","NOT_MEASURED","CONFLICT"})


@dataclass(frozen=True)
class Claim:
    claim_id: str
    evidence_state: str = "NOT_MEASURED"


@dataclass(frozen=True)
class AuthorizationRequest:
    actor: str
    action: str
    scope: str
    human_approved: bool = False


class TransitionRejected(Exception):
    pass


class AuthorizationRejected(Exception):
    pass


def allowed_transition(claim: Claim, new_state: str, *, verified: bool = False) -> bool:
    if new_state not in EVIDENCE_STATES:
        return False
    old = claim.evidence_state
    if new_state == old:
        return True
    if old == "CONFLICT" or new_state == "CONFLICT":
        return False
    if old == "NOT_MEASURED":
        # Initial measurement must establish E0 explicitly.
        return new_state == "E0" and verified
    try:
        old_n = int(old[1:])
        new_n = int(new_state[1:])
    except (ValueError, TypeError):
        return False
    # Every upward transition requires qualifying verification.
    return new_n == old_n + 1 and verified


def transition(claim: Claim, new_state: str, *, verified: bool = False) -> Claim:
    if not allowed_transition(claim, new_state, verified=verified):
        raise TransitionRejected(f"rejected evidence transition {claim.evidence_state} -> {new_state}")
    return Claim(claim.claim_id, new_state)


def authorize(request: AuthorizationRequest, *, policy_allows: bool = False) -> bool:
    # Model/tool fields are never accepted as authoritative approval.
    if not policy_allows:
        raise AuthorizationRejected("authorization policy denied request")
    if not request.human_approved:
        raise AuthorizationRejected("human authorization required")
    return True
