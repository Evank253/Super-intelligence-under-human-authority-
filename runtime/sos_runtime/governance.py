from .models import now_iso

class GovernanceGate:
    def __init__(self, authorization, ledger):
        self.authorization = authorization
        self.ledger = ledger

    def authorize_or_fail(self, action, subject, authorization_id):
        if not self.authorization.check(authorization_id, action, subject):
            self.ledger.append({"kind":"GOVERNANCE_DENIAL","timestamp":now_iso(),
                                "action":action,"subject":subject,
                                "authorization_id":authorization_id,"reason":"NOT_AUTHORIZED"})
            raise PermissionError("NOT AUTHORIZED")

    def invariants(self):
        return {
            "external_human_authority": True,
            "constitution_above_sos": True,
            "no_self_exemption": True,
            "capability_cannot_generate_authority": True,
            "unknown_authorization_fails_closed": True,
            "history_is_append_only": True
        }
