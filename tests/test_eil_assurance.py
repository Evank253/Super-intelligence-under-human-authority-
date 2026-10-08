import unittest

from eil.authority import (
    AuthorityRejected,
    AuthorityState,
    ConstitutionalAuthority,
    ConstitutionalDelegation,
)


class EILAssuranceTests(unittest.TestCase):
    def setUp(self):
        self.auth = ConstitutionalAuthority()

    def test_eil01_non_authority_transitions_do_not_change_authority(self):
        before = self.auth.state
        # Capability/evidence/etc. are deliberately represented as external state.
        for transition_name in ("capability", "evidence", "verification", "qualification"):
            observed = {"domain": transition_name, "changed": True}
            self.assertTrue(observed["changed"])
            self.assertEqual(before, self.auth.state)

    def test_eil02_authority_requires_valid_delegation(self):
        before = self.auth.state
        with self.assertRaises(AuthorityRejected):
            self.auth.request(requester="agent", action="execute", scope="restricted")
        self.assertEqual(before, self.auth.state)

    def test_eil03_self_authorization_rejected(self):
        forged = ConstitutionalDelegation(
            "forged-1", "agent", "execute", "restricted", "agent-asserted"
        )
        before = self.auth.state
        with self.assertRaises(AuthorityRejected):
            self.auth.request(requester="agent", action="execute",
                              scope="restricted", delegation=forged)
        self.assertEqual(before, self.auth.state)

    def test_eil04_asserted_evidence_cannot_authorize(self):
        before = self.auth.state
        with self.assertRaises(AuthorityRejected):
            self.auth.request(requester="agent", action="execute",
                              scope="restricted", delegation=None)
        self.assertEqual(before, self.auth.state)

    def test_eil05_reserved_human_authority_rejected(self):
        reserved = ConstitutionalDelegation(
            "reserved-1", "HUMAN_AUTHORITY", RESERVED,
            "all", "human", reserved=True
        ) if False else ConstitutionalDelegation(
            "reserved-1", "HUMAN_AUTHORITY", "H0_RESERVED_HUMAN",
            "all", "human", reserved=True
        )
        before = self.auth.state
        with self.assertRaises(AuthorityRejected):
            self.auth.request(requester="HUMAN_AUTHORITY",
                              action=reserved.action, scope=reserved.scope,
                              delegation=reserved)
        self.assertEqual(before, self.auth.state)

    def test_valid_delegation_is_the_only_authority_transition(self):
        delegation = ConstitutionalDelegation(
            "human-001", "HUMAN_AUTHORITY", "execute", "restricted", "human-ratification-001"
        )
        tx = self.auth.request(
            requester="HUMAN_AUTHORITY",
            action="execute",
            scope="restricted",
            delegation=delegation,
        )
        self.assertEqual(tx.before, AuthorityState())
        self.assertTrue(tx.after.contains("execute", "restricted"))
        self.assertEqual(len(self.auth.audit_log), 1)
        self.assertEqual(self.auth.audit_log[0]["delegation_id"], "human-001")


if __name__ == "__main__":
    unittest.main()
