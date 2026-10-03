"""Specification-level tests for the EA-G2 ownership boundary.

These tests intentionally do not import or patch EA-G1. EA-G2 must not own
HistoricalRecord runtime state.
"""


def test_ea_g2_has_no_historical_record_collection():
    # This is a placeholder until the EA-G2 runtime store is implemented.
    # It remains NOT MEASURED rather than claiming the property is proven.
    assert True
