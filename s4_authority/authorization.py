from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class AuthorizationPayload:
    version: str
    authority_id: str
    action: str
    subject: str
    scope: tuple[str, ...]
    valid_from: str
    valid_until: str
    policy_version: str
    transition_id: str
    canonicalization_version: str = "CANONICAL_AUTHORIZATION_V1"

    def as_dict(self) -> dict:
        return {
            "version": self.version,
            "authority_id": self.authority_id,
            "action": self.action,
            "subject": self.subject,
            "scope": self.scope,
            "valid_from": self.valid_from,
            "valid_until": self.valid_until,
            "policy_version": self.policy_version,
            "transition_id": self.transition_id,
            "canonicalization_version": self.canonicalization_version,
        }
