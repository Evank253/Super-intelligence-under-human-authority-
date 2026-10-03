# SoS Benchmark Harness

Status: IMPLEMENTED REFERENCE HARNESS — NOT SYSTEM QUALIFICATION.

This black-box harness tests the executable SoS boundary: runtime health, provenance indexing, evidence recording, fail-closed authorization, bounded execution, revocation, and additive re-indexing.

Run:
```
python3 benchmark/sos_benchmark.py
```

Live runtime:
```
PYTHONPATH=runtime python3 -m sos_runtime
```

The harness deliberately separates implementation behavior from intelligence, qualification, and constitutional authority claims. Real KCN, MANIFEX, BI, KSI, and Sister/Twin adapters must remain independently scoped.
