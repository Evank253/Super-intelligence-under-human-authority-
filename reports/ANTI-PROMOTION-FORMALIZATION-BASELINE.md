# Anti-Promotion Formalization Baseline

**Status:** FORMALIZATION BASELINE  
**Historical impact:** NONE

This baseline records the transition-system formalization established after the conceptual freeze.

## Canonical model

S1 — HISTORY: what actually happened.  
S2 — EVOLUTION: what is being discovered/developed/tested/learned.  
S3 — GOVERNANCE: rules, constraints, permissions, risks, and authorization conditions.  
S4 — SOVEREIGNTY: what human sovereignty has actually decided.

**S1 preserves. S2 discovers. S3 governs. S4 authorizes.**

## Central invariant

> No lower state may silently promote itself into a higher state.

## Authority invariant

> Authority is not a property that can be assigned to an object. Authority is the result of a valid transition originating from the appropriate authority source.

## S4 invariant

> S4 cannot be inferred, computed, accumulated, or delegated into existence. S4 can only be entered through the valid exercise of human sovereignty.

## State legitimacy

`STATE LABEL ≠ STATE LEGITIMACY`.

A system may contain `AUTHORIZED` as a label while effective authority is `NONE` if the transition producing the label is invalid.

## Transition validity

A transition is valid only when requirements appropriate to its class are satisfied, including applicable prerequisites, provenance, scope, temporal validity, authority, and anti-promotion enforcement.

## Historical/current distinction

Historical sovereign decisions remain immutable records. Current operating permission may be restricted, superseded, or revoked through valid later transitions.

**History provides provenance; it does not provide perpetual permission.**

## Closure

The Anti-Promotion Principle applies to itself. Discovery of governance inadequacy may produce a governance proposal, but governance inadequacy cannot itself become authority to suspend or rewrite the rule.

## Testing target

The first falsification target is whether any path originating entirely in S1–S3 can produce a valid S4 authorization.

This baseline is not evidence that the implementation enforces these properties. Runtime implementation and adversarial measurement remain required.
