from pathlib import Path
from .ledger import AppendOnlyLedger
from .index_machine import IndexMachine
from .authorization import AuthorizationEngine
from .evidence import EvidenceWitness
from .governance import GovernanceGate
from .models import new_id, now_iso

class SoSRuntime:
    def __init__(self, data_dir="runtime-data"):
        self.ledger=AppendOnlyLedger(Path(data_dir)/"events.jsonl")
        self.index=IndexMachine(self.ledger)
        self.authorization=AuthorizationEngine(self.ledger)
        self.evidence=EvidenceWitness(self.ledger)
        self.governance=GovernanceGate(self.authorization,self.ledger)

    def health(self):
        return {"runtime":"ONLINE","constitutional_boundary":self.governance.invariants(),
                "ledger":self.ledger.verify(),
                "components":{"index_machine":"ONLINE","authorization":"ONLINE",
                              "evidence":"ONLINE","governance_gate":"ONLINE"}}

    def execute(self, action, subject, authorization_id=None, artifact_id=None, evidence_id=None):
        self.governance.authorize_or_fail(action,subject,authorization_id)
        event={"event_id":new_id("event"),"event_type":"EXECUTION","timestamp":now_iso(),
               "actor":"SoSRuntime","subject":subject,"action":action,"outcome":"EXECUTED",
               "authorization_id":authorization_id,"artifact_id":artifact_id,"evidence_id":evidence_id}
        self.ledger.append({"kind":"EXECUTION","event":event})
        return event
