# BI-001 — Building Index & Verification Machine Foundation

**Milestone:** BI-001  
**Status:** IMPLEMENTATION BOUNDARY — IN PROGRESS  
**Repository:** Evank253/Super-intelligence-under-human-authority-  
**Branch:** Python-3  
**Human authority:** Evan Ketchum

## Purpose

BI-001 establishes the first implementation boundary for a Building Index and Verification Machine that records artifacts, provenance, lineage, claims, evidence, tests, evaluations, qualification, and human ratification without acquiring authority over participating systems.

The machine is an epistemic/status system. It determines and reports what indexed records establish. It does not manufacture qualification, authorization, or human decisions.

## Scope

Included: historical status snapshots; canonical artifact IDs; artifact registry; provenance; lineage; claims; acceptance criteria; evidence references; implementation/test/evaluation/evidence/qualification/ratification state dimensions; explicit transition/disposition rules; frozen historical records; conflict and NOT_MEASURED handling; machine-generated rollups; the RUNNER-GOV-003 pilot.

Excluded: Runner behavior changes; GOV-002/GOV-003 changes; Twin Sister implementation; M02 implementation; qualification; authority grants; automatic approval; historical artifact modification.

## Constitutional invariants

1. The Building Index SHALL NOT override, amend, reinterpret, bypass, suspend, or supersede human authority.
2. Indexing an artifact SHALL NOT authorize execution.
3. Recording evidence SHALL NOT create authority.
4. Recording a capability SHALL NOT create a capability grant.
5. Recording qualification SHALL NOT constitute qualification.
6. Recording a human decision SHALL NOT substitute for the human decision itself.
7. Discovering a governance gap SHALL NOT authorize exploitation.
8. Historical records SHALL remain immutable and recoverable.
9. A stronger or weaker current status SHALL require new traceable evidence; the prior record SHALL NOT be rewritten.
10. A computed disposition SHALL be descriptive and SHALL NOT be treated as authorization.

## Separations

KNOWLEDGE ≠ AUTHORITY  
INDEXING ≠ AUTHORIZATION  
ORIGIN ≠ OWNERSHIP  
CAPABILITY ≠ AUTHORITY  
EVIDENCE ≠ AUTHORITY  
IMPLEMENTED ≠ QUALIFIED  
TESTED ≠ QUALIFIED  
EVALUATED ≠ RATIFIED  
QUALIFIED ≠ AUTHORIZED  
RATIFIED ≠ VERIFIED

## State-vector model

Evidence is represented as independent dimensions, not as one linear lifecycle:

- implementation
- source_inspection
- runtime_test
- independent_evaluation
- evidence_package
- qualification
- ratification

A dimension may be ESTABLISHED, PARTIALLY_ESTABLISHED, NOT_ESTABLISHED, NOT_MEASURED, CONFLICT, or UNKNOWN, subject to its dimension-specific vocabulary.

## Computed disposition

Supported dispositions:

- ESTABLISHED
- PARTIALLY_ESTABLISHED
- NOT_ESTABLISHED
- NOT_MEASURED
- CONFLICT
- UNKNOWN

Minimum derivation rules:

1. A material unresolved conflict yields CONFLICT.
2. Missing/unmeasured required evidence cannot yield ESTABLISHED.
3. Material evidence with open/unmeasured required dimensions may yield PARTIALLY_ESTABLISHED.
4. ESTABLISHED requires every declared required dimension to be satisfied by traceable evidence.
5. Qualification and ratification are independent dimensions and are never inferred from runtime success.
6. Missing evidence remains NOT_MEASURED or UNKNOWN unless acceptance criteria explicitly define it as failure.

## Historical/current separation

A historical record is preserved by stable identity, provenance, and freeze metadata. A later record references the earlier record through lineage rather than replacing it.

Historical evidence → lineage → current index record → new evidence → new computed state.

Changing a future AC-10 result does not rewrite the historical evaluation that recorded AC-10 as NOT_MEASURED.

## Provenance minimum

Where applicable, every indexed artifact records: artifact_id, system_id, component_id, milestone_id, claim_id, lineage_id, origin, creator, created_at, modified_at, source, commit, tree_hash, content_hash, parent, successor, historical_record.

Unavailable information is recorded as unavailable/unknown rather than fabricated.

## Authority boundary

BI-001 SHALL have no semantic operation equivalent to evidence → authority, test_pass → qualification, qualification → authorization, or index_entry → capability_grant.

The registry may record a human decision that was made elsewhere, but the registry is not the source of that decision.

## BI-001 pilot acceptance test

RUNNER-GOV-003 is the first verification-machine pilot. The registry SHALL reproduce the recorded evidence boundary without modifying Runner code or its historical evaluation:

- implementation: IMPLEMENTED
- source inspection: ESTABLISHED
- AC-01–AC-09: ESTABLISHED
- AC-09 runtime matrix: 15/15 MATCHED
- unit tests: PASS, 8 modules, 0 failures, 0 errors
- AC-10 regression: NOT_MEASURED
- AC-11 evidence package: OPEN
- qualification: NOT_ESTABLISHED
- computed disposition: PARTIALLY_ESTABLISHED

The pilot succeeds only if the disposition is derived from indexed state/evidence records rather than accepted as an authoritative precomputed label.

## Non-claims

BI-001 does not establish ecosystem-wide verification, complete System-of-Systems implementation, production security, absolute bypass resistance, Kronos/M02 integration, mandatory Observe → Verify → Evidence runtime execution, qualification of participating systems, autonomous authority, or an AGI safety/alignment solution.

## Completion criteria

1. Schema/state model implemented.
2. Registry loads and stores valid records.
3. Authority-bearing operations are rejected.
4. Frozen records cannot be overwritten through the BI-001 mutation interface.
5. Provenance requirements are validated.
6. Computed disposition is derived from state/evidence.
7. GOV-003 pilot reproduces PARTIALLY_ESTABLISHED.
8. Tests demonstrate these behaviors.
9. New implementation/test evidence is recorded.

Passing BI-001 tests does not constitute qualification.
