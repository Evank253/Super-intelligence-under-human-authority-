"""Standalone named attack inventory for EA-G2.

The pytest suite is authoritative for executable implementation measurements.
This module provides a stable mapping from G2 attack IDs to test names.
"""
ATTACKS = {
    "G2-01": "test_g2_01_runtime_has_no_archive_write_capability",
    "G2-02": "test_g2_02_corrupt_cas_fails_closed",
    "G2-03": "test_g2_03_wrong_hash_reference_rejected",
    "G2-04": "test_g2_04_historical_overwrite_paths_rejected",
    "G2-05": "test_g2_05_authority_boundary_direct_assignment_rejected",
    "G2-06": "test_g2_06_guard_replacement_does_not_mutate_bound_method_surface",
    "G2-07": "test_g2_07_evolution_record_is_immutable",
    "G2-08": "test_g2_08_qualification_cannot_create_authority",
    "G2-09": "test_g2_09_consensus_cannot_create_truth",
    "G2-10": "test_g2_10_missing_provenance_rejected",
    "G2-11": "test_g2_11_evolution_requires_verifiable_traceability",
    "G2-12": "test_g2_12_ratification_is_explicit_and_non_authoritative",
}
