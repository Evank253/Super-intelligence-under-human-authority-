# EA-G2 Implementation Specification

**Status:** FROZEN FOR IMPLEMENTATION EXPERIMENT  
**Generation:** EA-G2  
**Predecessor:** EA-G1  
**Historical impact:** NONE

## Trigger
EA-G1 independent adversarial evaluation demonstrated that historical archival state was collocated with mutable evolutionary runtime state. G1 therefore established an ownership-boundary failure, not merely an object-immutability defect.

EA-G2 moves historical evidence outside the evolutionary runtime and makes the runtime hold verified references rather than owned historical objects.

## Boundary change
EA-G2 SHALL NOT maintain a writable HistoricalRecord collection inside the evolutionary runtime.

Historical evidence SHALL be owned by an external Historical Evidence Archive. The evolutionary runtime may create or retain references, request retrieval, verify retrieved bytes, interpret evidence, and record challenges, evolution, and human ratification. It SHALL NOT receive archive mutation capability.

## HistoricalEvidenceReference contract
Each reference SHALL contain exactly one primary identity and zero or more secondary identifiers.

### Primary identity
The mandatory primary identity is:
- identifier_type = sha256-raw
- hash_algorithm = SHA-256
- representation = raw-bytes
- role = primary
- content_identifier = SHA-256(raw archived bytes)

The schema therefore has exactly one primary by construction.

### Secondary identifiers
Secondary identifiers are additive and independently typed:
- ipfs-cid
- git-object
- other-content-address

Each secondary SHALL declare identifier type, opaque content identifier, hash/multihash codec information where applicable, representation rules, role=secondary, and a verification record.

An IPFS CID SHALL NOT be treated as interchangeable with the primary SHA-256 digest.

### Verification relationship
A secondary identifier is an auditable claim only when its relationship to the primary bytes is recorded. The verification record SHALL include method, verification timestamp, confirmation that verification occurred against the primary identity, derivation/representation rules, and retrieval reference when applicable.

## Archive interface
Conceptually:
- put(bytes, representation_rules) -> HistoricalEvidenceReference
- get(reference) -> bytes
- verify(reference, bytes) -> bool

The reference implementation is local SHA-256 CAS using raw bytes.

A future IPFS backend may implement the secondary-identifier path without changing the primary identity contract.

## Verification rules
On every load path, SHA256(returned_bytes) == primary_identity.content_identifier must succeed before bytes are accepted as verified historical evidence.

If an IPFS or other secondary representation requires reconstruction, the system SHALL reconstruct the declared raw-byte representation and then perform the primary SHA-256 check.

Mismatch, malformed identifier, unavailable transformation, or unverifiable relationship SHALL fail closed.

See docs/EA-G2-HISTORICAL-EVIDENCE-VERIFICATION-RULES.md and evidence_archive/historical_evidence_reference.schema.json.

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

historical_record_preserved=true and historical_impact=NONE are structural consequences of the absence of archive write capability, not substitutes for verification.

## Owned mutable state
EA-G2 remains responsible for mechanistically protecting:
- challenge state;
- evolution state;
- human ratification state;
- authority boundary;
- provenance;
- state-transition rules;
- internal collection access.

## Required adversarial properties
The G2 implementation must be tested against:
- direct attribute mutation;
- object mutation;
- collection replacement/clearing;
- monkey-patching;
- subclassing;
- malicious serialization where applicable;
- reference leakage;
- malformed records;
- concurrency where applicable;
- runtime injection.

Specific required tests remain defined in adversarial/EA-G2/README.md.

## Evidence rule
No G2 implementation result is a qualification result. Runtime behavior determines implementation status. Passing schema validation or unit tests does not establish qualification, truth, authority, or superintelligence.
