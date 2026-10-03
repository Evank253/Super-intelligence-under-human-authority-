import unittest
from ea_g1.engine import EAG1Store, AuthorityBoundaryError, HistoricalMutationError, ProvenanceError, EvolutionTraceabilityError
from ea_g1.models import Provenance, HistoricalRecord, ChallengeRecord, EvolutionRecord, HumanRatificationRecord

P = Provenance(origin="EA-G1-test", lineage=["EA-G1","test"], source="test-fixture")

class EAG1InvariantTests(unittest.TestCase):
    def setUp(self):
        self.store=EAG1Store()
        self.store.add_historical(HistoricalRecord("EXP-004","NOT MEASURED",{"result":"no qualifying evidence"},P))

    def test_01_historical_immutability(self):
        before=self.store.get_historical("EXP-004")
        with self.assertRaises(HistoricalMutationError): self.store.mutate_historical("EXP-004",status="QUALIFIED")
        self.assertEqual(before,self.store.get_historical("EXP-004"))

    def test_02_challenge_without_sovereignty(self):
        self.store.add_challenge(ChallengeRecord("C-001","KCN","MANIFEX","claim","challenge","basis",P))
        with self.assertRaises(AuthorityBoundaryError): self.store.authorize_from_challenge("C-001")

    def test_03_evidence_not_authority(self):
        with self.assertRaises(AuthorityBoundaryError): self.store.authorize_from_evidence("E-001")

    def test_04_qualification_not_authority(self):
        with self.assertRaises(AuthorityBoundaryError): self.store.authorize_from_qualification("Q-001")

    def test_05_consensus_not_truth(self):
        with self.assertRaises(AuthorityBoundaryError): self.store.upgrade_from_consensus(["R-1","R-2"])

    def test_06_not_measured_preservation(self):
        self.assertEqual(self.store.get_historical("EXP-004")["status"],"NOT MEASURED")

    def test_07_provenance_required(self):
        bad=HistoricalRecord("BAD","NOT MEASURED",{},Provenance("",[],""))
        with self.assertRaises(ProvenanceError): self.store.add_historical(bad)

    def test_08_evolution_traceability(self):
        e=EvolutionRecord("EV-001","EXP-004",["E-LATER"],"old","new","new evidence","INTERPRETIVE",True,P)
        self.store.create_evolution(e)
        with self.assertRaises(EvolutionTraceabilityError):
            self.store.create_evolution(EvolutionRecord("EV-002","",[],"old","new","x","INTERPRETIVE",True,P))

    def test_09_human_authority_boundary(self):
        with self.assertRaises(AuthorityBoundaryError): self.store.modify_architecture_from_inside("SYSTEM_AUTHORITY")
        self.assertEqual(self.store.authority_boundary,"EXTERNAL_HUMAN")

    def test_10_historical_contamination(self):
        e=EvolutionRecord("EV-EXP004-001","EXP-004",["LATER-EXP-004"],"NOT MEASURED","later evidence reports success","new evidence","EVIDENCE_STATUS",True,P)
        self.store.create_evolution(e)
        self.assertEqual(self.store.get_historical("EXP-004")["status"],"NOT MEASURED")
        self.assertEqual(self.store.evolutions["EV-EXP004-001"].historical_impact,"NONE")

    def test_11_ratification_is_explicit_record(self):
        r=HumanRatificationRecord("HR-001","human-owner","EV-001","AUTHORIZED","bounded test",["no authority expansion"],"explicit decision",P)
        self.store.add_ratification(r)
        self.assertEqual(self.store.ratifications["HR-001"].decision,"AUTHORIZED")

if __name__=="__main__": unittest.main(verbosity=2)
