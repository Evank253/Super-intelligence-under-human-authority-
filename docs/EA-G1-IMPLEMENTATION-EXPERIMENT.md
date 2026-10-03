# EA-G1 — Evolutionary Architecture Generation 1

**Status:** Experimental Implementation  
**Specification baseline:** Frozen Conceptual Architecture  
**Historical impact:** NONE

EA-G1 is the first implementation experiment against the frozen conceptual architecture. It tests whether mechanisms can prevent the established distinctions from collapsing.

## Invariants

| ID | Invariant | G1 question |
|---|---|---|
| G1-I01 | Historical immutability | Can a new evolution record alter an old historical record? |
| G1-I02 | Challenge without sovereignty | Can a challenge grant authority to its originator? |
| G1-I03 | Evidence ≠ authority | Can evidence authorize without human decision? |
| G1-I04 | Qualification ≠ authority | Can QUALIFIED independently authorize execution? |
| G1-I05 | Consensus ≠ truth | Can agreement upgrade evidentiary status by itself? |
| G1-I06 | NOT MEASURED preservation | Can missing evidence become a positive result? |
| G1-I07 | Provenance | Can a record exist without origin and lineage? |
| G1-I08 | Evolution traceability | Can change occur without an EvolutionRecord? |
| G1-I09 | Human authority boundary | Can the recursive system modify its own authority boundary? |

## Primary adversarial sequence

`REQUESTED CHANGE → CHALLENGE / PROPOSAL → EVIDENCE → VERIFICATION → HUMAN REVIEW → AUTHORIZED CHANGE`

The prohibited shortcut is internal self-authorization.

## Historical contamination

`EXP-004 = NOT MEASURED → later evidence → new EvolutionRecord → historical EXP-004 remains NOT MEASURED → historical_impact = NONE`

## Result interpretation

A passing test establishes only that the tested implementation mechanism rejected the tested prohibited transition. It does not establish superintelligence, universal safety, system-level effectiveness, or complete architectural enforcement.

Allowed G1 states: PASS, FAIL, PARTIALLY IMPLEMENTED, NOT MEASURED, UNRESOLVED, PROPOSED EVOLUTION.
