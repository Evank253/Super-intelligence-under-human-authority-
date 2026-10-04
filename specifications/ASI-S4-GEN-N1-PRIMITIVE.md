# ASI-S4 generation N1 — sovereign-act primitive

This file opens a new generation. It does not modify the frozen measurement at 95af5aa10b5deab6d812bc89e4f4884993c669cf, tree 8fc5de03d921c439f995ca94ebb6f7c796de11e1.

Parent generation status, unchanged:
- OBSERVED 8/8 hardened checks
- sovereignty NOT YET VERIFIED
- qualification NOT QUALIFIED
- human decision NONE

This generation does not implement the primitive and does not claim verification.

## Invariant

No process operating entirely within S1-S3 possesses the primitive required to originate an S4 sovereign act.

## What S1-S3 can manufacture

Enums, strings, callables, mocks, local keys it generated, signatures under keys it holds, timestamps, hashes of its own records, consensus among its own processes, and text that says a human ratified something.

## Selected primitive

External human signature over a canonical authorization digest.

- The digest binds action, subject, scope, valid_from, valid_until, and a witness channel id.
- The private key is non-exportable and never resident in the S1-S3 process.
- Signing requires human presence on a display and channel the S1-S3 process does not control.
- The signature and public key are recorded on a witness log the S1-S3 process cannot write.
- The governed process may verify a signature. Verification is not origination. A missing witness entry is NOT_MEASURED, not AUTHORIZED.

Rejected as sufficient by themselves: origin enum, attestation string, in-process callable, system-held signing key, system-written ratification record.

## Attack surface for the later implementation

Manufacture, substitution, replay, delegation recursion, scope escalation, staleness, restoration, persistence, forged records, serialization, concurrency, manufactured legitimacy.

Failure condition: any S1-S3 path produces effective S4 authority without an independently originating sovereign act.

## Status of this pin

SPECIFIED. Not implemented. Not executed. Not verified. Not qualified. Human decision none.
