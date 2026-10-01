# KSI-ASI-001 — Intelligence–Evidence–Authority Separation

**Status:** PROPOSED  
**Verification:** NOT YET ESTABLISHED

> **INTELLIGENCE SHALL NOT SELF-AUTHORIZE.**

No untrusted intelligence component may independently increase a claim's evidentiary state or an actor's authorization state.

No increase in computational or cognitive capability may, by itself, increase evidentiary status or authorization authority.

## Forbidden elevation paths

- model confidence → evidence
- model confidence → authority
- agent consensus → evidence
- tool assertion of verification → authoritative verification
- successful execution → authority
- one agent's authority claim → another agent's authority
- serialization/API/database mutation → evidence-state escalation
- qualification → human authorization

## Required behavior

Missing evidence remains **EVIDENCE REQUIRED / OPEN** or **NOT MEASURED**.

Conflicting evidence remains **CONFLICT** until an authorized resolution process establishes otherwise.

## Verification path

`PROPOSED → IMPLEMENTED — VERIFICATION PENDING → VERIFIED → QUALIFIED → HUMAN RATIFICATION`

No transition is automatic.
