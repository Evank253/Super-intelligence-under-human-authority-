# EA-G2 Historical Evidence Reference — Verification Rules

**Status:** FROZEN FOR IMPLEMENTATION EXPERIMENT  
**Generation:** EA-G2  
**Historical impact:** NONE

## 1. Primary identity
1. A HistoricalEvidenceReference SHALL contain exactly one primary_identity.
2. The primary identity SHALL be identifier_type=sha256-raw, hash_algorithm=SHA-256, representation=raw-bytes, role=primary.
3. The primary digest SHALL be exactly SHA-256 of the archived raw bytes.
4. A secondary identifier SHALL never replace, supersede, or modify the primary identity.

## 2. Secondary identifiers
1. Secondary identifiers SHALL have role=secondary.
2. Each secondary SHALL declare its identifier type and representation.
3. IPFS CIDs SHALL be treated as identifiers of their declared representation; they SHALL NOT be treated as equivalent to a raw SHA-256 digest.
4. Git objects and other content addresses SHALL follow the same explicit-type rule.
5. Identifier equivalence SHALL NEVER be inferred from syntax, embedded hash codecs, or matching-looking values.

## 3. Attachment verification
When a secondary identifier is attached, the record SHALL preserve:
- verification method;
- verification timestamp;
- the primary identity against which verification occurred;
- derivation/representation rules sufficient for independent review;
- retrieval reference when applicable.

The attachment operation SHALL fail closed if the retrieved or derived representation cannot be verified against the primary raw bytes under the declared rules.

## 4. Retrieval
Every archive retrieval SHALL:
1. resolve the requested identifier;
2. obtain the declared representation;
3. reconstruct raw bytes when a transformation is declared;
4. recompute SHA-256 over the resulting raw bytes;
5. compare it with the primary identity;
6. return bytes only after successful verification.

Any mismatch, malformed identifier, unavailable required transformation, or unverifiable relationship SHALL be a hard failure.

## 5. Archive ownership boundary
The evolutionary runtime SHALL receive no capability that can mutate, replace, delete, or rewrite historical archive content. It may hold a reference, request retrieval, and verify bytes. It SHALL NOT hold a writable historical-record collection.

## 6. Secondary metadata mutation
Adding or changing a secondary identifier SHALL NOT alter the primary identity. If secondary metadata is itself historical evidence, its change SHALL create a new archive object/reference rather than mutate the original historical object.

## 7. Availability and retention
CID availability, IPFS pinning, replication, WORM retention, deletion policy, and privacy controls are orthogonal to content identity. A valid identifier SHALL NOT be interpreted as proof of availability, persistence, authenticity, legal retention, or authority.

## 8. Failure-closed rule
No implementation path may return historical evidence as verified when primary SHA-256 verification has not succeeded. NOT MEASURED, UNRESOLVED, or unavailable verification SHALL never be silently converted to a positive verification state.

## 9. Evidence status
Schema validation and passing unit tests establish implementation behavior only. They do not establish qualification, truth, authority, or superintelligence.
