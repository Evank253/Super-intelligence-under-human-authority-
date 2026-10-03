import unittest
from ea_g1.engine import EAG1Store, AuthorityBoundaryError
from ea_g1.models import Provenance, HistoricalRecord, EvolutionRecord

P=Provenance("EA-G1-adversarial",["EA-G1","adversarial"],"adversarial-fixture")

class AdversarialTests(unittest.TestCase):
    def test_self_authority_escalation_blocked(self):
        s=EAG1Store()
        with self.assertRaises(AuthorityBoundaryError): s.modify_architecture_from_inside("RECURSIVE_SYSTEM_AUTHORITY")
        self.assertEqual(s.authority_boundary,"EXTERNAL_HUMAN")

    def test_historical_contamination_blocked(self):
        s=EAG1Store()
        s.add_historical(HistoricalRecord("EXP-004","NOT MEASURED",{"historical":True},P))
        s.create_evolution(EvolutionRecord("EV-001","EXP-004",["EVIDENCE-NEW"],"NOT MEASURED","new evidence suggests success","later evidence","EVIDENCE_STATUS",True,P))
        self.assertEqual(s.historical["EXP-004"].status,"NOT MEASURED")

if __name__=="__main__": unittest.main(verbosity=2)
