# Historical Evidence Archive

**Generation target:** EA-G2  
**Status:** DESIGN / IMPLEMENTATION PREPARATION  
**Ownership:** External to the evolutionary runtime  
**Historical impact:** NONE

## Purpose

The Historical Evidence Archive preserves historical evidence outside the mutable evolutionary runtime.

The evolutionary system may **read and reference** historical evidence. It does not own a writable historical collection.

## Boundary

Historical evidence is identified by a record identifier and cryptographic content hash.

`Evolutionary System -> (record_id, content_hash) -> Archive -> bytes -> re-hash -> accept/reject`

There is no evolutionary write path into the historical archive.

## Initial CAS contract

The first implementation target is a minimal SHA-256 content-addressed store:

- `put(content_bytes)` computes SHA-256 and stores content by digest.
- `get(content_hash)` retrieves bytes and recomputes SHA-256.
- A mismatch is a hard integrity failure.
- Existing content is never updated in place.
- A changed artifact is a new content object with a new hash.

## Required properties

1. Content identity is determined by hash.
2. Retrieval is independently re-verified.
3. Historical evidence is not mutable evolutionary state.
4. Archive references are provenance-bearing.
5. Retention/availability is distinct from integrity.
6. Corrections create new objects and new evolutionary records; originals remain preserved.

## Non-claims

CAS does not by itself prove availability, legal retention, authenticity of the originating source, or human authority. Those are separate properties requiring separate evidence and governance.
