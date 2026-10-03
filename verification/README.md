# BI-001 Verification Implementation

This directory contains the initial executable BI-001 foundation.

The implementation is intentionally narrow: append-only artifact registration, provenance validation, frozen historical record protection, explicit lineage, state-vector disposition computation, rejection of authority-bearing registry operations, and GOV-003 pilot reproduction.

Run from this directory:

    python -m unittest discover -s . -v

Passing these tests establishes only the behavior measured by these tests. It does not qualify BI-001 or any indexed system.
