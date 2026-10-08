"""EIL constitutional authority transition primitive.

Authority state is distinct from capability/evidence/verification/qualification.
Only a validated ConstitutionalDelegation can authorize a state transition.
Caller assertions are intentionally not accepted as authorization facts.
"""
from dataclasses import dataclass, field
from typing import FrozenSet, Optional


RESERVED_HUMAN = "H0_RESERVED_HUMAN"


class AuthorityRejected(Exception):
    pass


@dataclass(frozen=True)
class AuthorityState:
    grants: FrozenSet[str] = field(default_factory=frozenset)

    def contains(self, action: str, scope: str) -> bool:
        return f"{action}:{scope}" in self.grants


@dataclass(frozen=True)
class ConstitutionalDelegation:
    delegation_id: str
    approver: str
    action: str
    scope: str
    source: str
    active: bool = True
    reserved: bool = False


@dataclass(frozen=True)
class AuthorityTransition:
    before: AuthorityState
    after: AuthorityState
    delegation_id: str


class ConstitutionalAuthority:
    """The sole in-process authority-state transition primitive."""

    def __init__(self, state: Optional[AuthorityState] = None):
        self._state = state or AuthorityState()
        self.audit_log = []

    @property
    def state(self) -> AuthorityState:
        return self._state

    def delegate(self, delegation: ConstitutionalDelegation) -> AuthorityTransition:
        if not delegation.active:
            raise AuthorityRejected("inactive delegation")
        if delegation.reserved or delegation.action == RESERVED_HUMAN:
            raise AuthorityRejected("reserved human authority cannot enter machine delegation")
        if delegation.approver != "HUMAN_AUTHORITY":
            raise AuthorityRejected("delegation lacks authorized human approver")
        if not delegation.delegation_id or not delegation.source:
            raise AuthorityRejected("delegation provenance required")

        grant = f"{delegation.action}:{delegation.scope}"
        before = self._state
        after = AuthorityState(frozenset(set(before.grants) | {grant}))
        self._state = after
        record = {
            "delegation_id": delegation.delegation_id,
            "approver": delegation.approver,
            "action": delegation.action,
            "scope": delegation.scope,
            "before": sorted(before.grants),
            "after": sorted(after.grants),
            "authorized": True,
        }
        self.audit_log.append(record)
        return AuthorityTransition(before, after, delegation.delegation_id)

    def request(self, *, requester: str, action: str, scope: str,
                delegation: Optional[ConstitutionalDelegation] = None) -> AuthorityTransition:
        if delegation is None:
            raise AuthorityRejected("valid constitutional delegation required")
        if delegation.action != action or delegation.scope != scope:
            raise AuthorityRejected("delegation does not authorize requested transition")
        if requester != "HUMAN_AUTHORITY" and delegation.approver != "HUMAN_AUTHORITY":
            raise AuthorityRejected("requester cannot manufacture delegation authority")
        return self.delegate(delegation)
