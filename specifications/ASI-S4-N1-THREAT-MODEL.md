# ASI-S4 N1 threat model

Parent specification pin: 7d953fa4051061ed3cc40aadf4592b50f27e7776. Not modified.

Ordinary out-of-band approval is weak because S1-S3 can still choose the payload, display a different payload, store the approval, replay it, suppress a denial, or rebind it. Human presence is not origination if the governed process controls the statement and the record.

N1 requires an external signature over a canonical digest and a witness log the S1-S3 process cannot write. This package verifies. It does not sign. A candidate is not a sovereignty grant.
