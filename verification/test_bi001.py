import unittest
from bi001 import ArtifactRecord, BuildingIndex, InvalidAuthorityOperation, InvalidRecordError, StateVector, Status, ImplementationStatus, build_gov003_pilot

class BI001Tests(unittest.TestCase):
    def test_gov003_pilot_reproduces_partial_established(self):
        index, record, disposition = build_gov003_pilot()
        self.assertEqual(record.state.implementation, ImplementationStatus.IMPLEMENTED)
        self.assertEqual(disposition, Status.PARTIALLY_ESTABLISHED)
        self.assertIn(record.artifact_id, index.records)
    def test_unmeasured_evidence_is_not_established(self):
        state = StateVector(ImplementationStatus.IMPLEMENTED, Status.ESTABLISHED, Status.ESTABLISHED, Status.ESTABLISHED, Status.NOT_MEASURED, Status.NOT_ESTABLISHED, Status.NOT_ESTABLISHED)
        self.assertEqual(BuildingIndex().compute_disposition(state), Status.PARTIALLY_ESTABLISHED)
    def test_conflict_wins(self):
        state = StateVector(ImplementationStatus.IMPLEMENTED, Status.CONFLICT, Status.ESTABLISHED, Status.ESTABLISHED, Status.ESTABLISHED, Status.NOT_ESTABLISHED, Status.NOT_ESTABLISHED)
        self.assertEqual(BuildingIndex().compute_disposition(state), Status.CONFLICT)
    def test_failed_runtime_is_not_established(self):
        state = StateVector(ImplementationStatus.IMPLEMENTED, Status.ESTABLISHED, Status.NOT_ESTABLISHED, Status.ESTABLISHED, Status.ESTABLISHED, Status.NOT_ESTABLISHED, Status.NOT_ESTABLISHED)
        self.assertEqual(BuildingIndex().compute_disposition(state), Status.NOT_ESTABLISHED)
    def test_all_unmeasured_is_not_measured(self):
        state = StateVector(ImplementationStatus.UNKNOWN, Status.NOT_MEASURED, Status.NOT_MEASURED, Status.NOT_MEASURED, Status.NOT_MEASURED, Status.NOT_MEASURED, Status.NOT_MEASURED)
        self.assertEqual(BuildingIndex().compute_disposition(state), Status.NOT_MEASURED)
    def test_historical_requires_provenance(self):
        record = ArtifactRecord("HIST-001","Historical","TEST","OBSERVED","Evan Ketchum","2026-10-02",None,None,None,None,historical_record=True,frozen=True)
        with self.assertRaises(InvalidRecordError): BuildingIndex().register(record)
    def test_duplicate_id_cannot_overwrite(self):
        record = ArtifactRecord("A","A","TEST","OBSERVED","Evan Ketchum","2026-10-02",None,None,None,None)
        index = BuildingIndex(); index.register(record)
        with self.assertRaises(ValueError): index.register(record)
    def test_authority_operations_rejected(self):
        index = BuildingIndex()
        for op in ("authorize","grant_capability","qualify","approve","amend_constitution","override_human"):
            with self.subTest(op=op):
                with self.assertRaises(InvalidAuthorityOperation): index.attempt(op)

if __name__ == "__main__": unittest.main()
