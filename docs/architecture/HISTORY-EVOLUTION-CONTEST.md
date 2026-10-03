# History, Evolution, and Independent Contest

**Status:** ARCHITECTURAL DESIGN

## 1. Separation

The SoS maintains separate functions for:
1. Historical preservation
2. Evolution
3. Independent contest
4. Evidence and verification
5. Human ratification

They interact, but they are not collapsed into one self-validating mechanism.

## 2. Historical Record

The Historical Record preserves the state established at a given point.

It records source, version, commit/tree/path where applicable, claims, evidence, tests, dispositions, unresolved conditions, ratification state, and supersession relationships.

Historical records are not retroactively promoted because later systems become more capable.

## 3. Evolution Record

The Evolution Record tracks:
- proposed changes;
- implementation changes;
- capability changes;
- governance changes;
- evidence supporting changes;
- systems affected;
- re-verification requirements;
- adoption decisions;
- human ratification where required.

Evolution is allowed and expected.

## 4. Contest mechanism

The architecture permits an independent mechanism or participating ecosystem to contest an evolutionary proposal.

Example:
Evolution proposes X
  -> history shows prior failure Y
  -> contest requests explanation
  -> new implementation/evidence supplied
  -> independent verification
  -> disposition
  -> human adoption when required

The historical failure is not erased. New evidence can establish that the relevant condition has changed.

## 5. No sole-judge principle

The component responsible for producing an evolutionary change should not automatically be the sole authority for declaring that change safe, verified, qualified, or constitutionally adopted.

Where practical, use independent witnessing, separate evidence paths, adversarial review, or another documented separation.

## 6. Disagreement

DISAGREEMENT
  -> PRESERVE
  -> IDENTIFY SCOPE
  -> TRACE PROVENANCE
  -> COLLECT EVIDENCE
  -> INDEPENDENT REVIEW
  -> RESOLVE / REMAIN OPEN / ESCALATE

The SoS must not silently discard disagreement.

## 7. Evolution is not authority

A successful evolutionary cycle establishes only the status supported by its evidence and governance process.

SUCCESSFUL EVOLUTION != CONSTITUTIONAL AUTHORITY

## 8. Objective

Historical/evolution separation does not freeze the system. It makes increasingly capable evolution auditable, contestable, reproducible where required, and constitutionally bounded.
