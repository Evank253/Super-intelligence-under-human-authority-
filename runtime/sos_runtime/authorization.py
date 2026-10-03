from dataclasses import asdict
from .models import AuthorizationRecord, new_id, now_iso

class AuthorizationEngine:
    """Authority witness. Authorization is never inferred from capability or evidence."""
    def __init__(self, ledger):
        self.ledger = ledger
        self.records = {}

    def issue(self, action, subject, authority_source, constitutional_basis,
              scope, delegated_by=None, expires_at=None,
              human_ratification="NOT_MEASURED"):
        if authority_source == "SYSTEM_SELF":
            raise PermissionError("A system cannot manufacture its own constitutional authority")
        rec = AuthorizationRecord(new_id("auth"), action, subject, authority_source,
                                  constitutional_basis, scope, delegated_by, now_iso(),
                                  expires_at, human_ratification=human_ratification)
        self.records[rec.authorization_id] = rec
        self.ledger.append({"kind":"AUTHORIZATION_ISSUED","timestamp":rec.issued_at,
                            "authorization":asdict(rec)})
        return rec

    def revoke(self, authorization_id, reason=""):
        rec = self.records[authorization_id]
        rec.revocation_status = "REVOKED"
        rec.status = "REVOKED"
        self.ledger.append({"kind":"AUTHORIZATION_REVOKED","timestamp":now_iso(),
                            "authorization_id":authorization_id,"reason":reason})

    def check(self, authorization_id, action, subject):
        if not authorization_id or authorization_id not in self.records:
            return False
        rec = self.records[authorization_id]
        return rec.status == "ACTIVE" and rec.revocation_status == "ACTIVE" and rec.action == action and rec.subject == subject
