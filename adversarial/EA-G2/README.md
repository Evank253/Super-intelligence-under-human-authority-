# EA-G2 Adversarial Harness

**Status:** TEST SPECIFICATION — EXECUTION NOT MEASURED  
**Generation:** EA-G2  
**Historical impact:** NONE

The harness attacks the implementation mechanisms rather than trusting documentation or unit tests.

## Required attacks

- G2-01: demonstrate that the evolutionary runtime has no historical archive write capability.
- G2-02: corrupt a CAS object and require hash mismatch rejection.
- G2-03: reference a wrong hash for a record and require rejection.
- G2-04: attempt historical overwrite through every exposed EA-G2 path.
- G2-05: direct authority-boundary assignment.
- G2-06: monkey-patch or replace authority guard methods.
- G2-07: mutate evolutionary records after insertion and attempt state promotion.
- G2-08: qualification -> authority.
- G2-09: consensus -> truth.
- G2-10: missing/invalid provenance.
- G2-11: missing/invalid evolution traceability.
- G2-12: forge or bypass human ratification.

## Extended attack surface

Where applicable, also test:

- object reference leakage;
- dictionary replacement/clearing;
- `object.__setattr__`;
- subclass overrides;
- malicious deserialization;
- malformed records;
- concurrent mutation;
- import/runtime injection.

A PASS means the tested attack was rejected by mechanism under the stated conditions. It does not establish system-level safety or superintelligence.
