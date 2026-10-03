# EA-G2 Implementation Specification

**Status:** FROZEN FOR IMPLEMENTATION EXPERIMENT  
**Generation:** EA-G2  
**Predecessor:** EA-G1  
**Historical impact:** NONE

## Trigger

EA-G1 independent adversarial evaluation demonstrated that historical archival state was collocated with mutable evolutionary runtime state.

This specification treats that result as implementation evidence and establishes a new implementation generation.

## Boundary change

EA-G2 SHALL NOT maintain a writable `HistoricalRecord` collection inside the evolutionary runtime.

Historical evidence SHALL be external to the evolutionary runtime and referenced by:

- `record_id`
- `content_hash`
- `hash_algorithm`

The evolutionary runtime may retrieve evidence for verification, but it shall not receive an archive mutation capability.

## CAS contract

Initial implementation uses SHA-256 content addressing.

For every retrieval:

`SHA256(returned_bytes) == referenced_content_hash`

Failure is a hard integrity error.

Changing historical content creates a different content address. Corrections are new evidence objects and new evolutionary records; original evidence remains preserved.

## EvolutionRecord contract

EA-G2 evolution records are interpretive records. They reference historical evidence rather than containing writable historical objects.

Required conceptual fields:

- evolution_id
- historical_reference
- historical_hash
- prior_interpretation
- new_evidence
- new_interpretation
- reason_for_change
- change_classification
- historical_record_preserved
- historical_impact
- optional human_ratification_id

`historical_record_preserved=true` and `historical_impact=NONE` are structural consequences of the absence of an archive write capability, not substitutes for verification.

## Owned mutable state

EA-G2 is responsible for mechanistically protecting:

- challenge state
- evolution state
- human ratification state
- authority boundary
- provenance
- state-transition rules
- internal collection access

## Required adversarial properties

The G2 implementation must be tested against direct attribute mutation, object mutation, collection replacement/clearing, monkey-patching, subclassing, and malicious serialization where applicable.

## Evidence rule

No G2 implementation result is a qualification result. Runtime behavior determines implementation status.
