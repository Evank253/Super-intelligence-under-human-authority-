# Transition Calculus & Anti-Promotion Specification

**Status:** FORMALIZATION BASELINE — IMPLEMENTATION REQUIRED  
**Scope:** S1–S4 state transitions, evidence/qualification/authorization boundaries, anti-promotion enforcement  
**Historical impact:** NONE. This specification adds a formalization layer and does not rewrite historical records.

## 1. Purpose

This specification defines state transition legitimacy as a first-class architectural property.

The architecture is not concerned only with whether a system currently displays a state label. It must establish whether the transition that produced that state was valid.

**STATE LABEL ≠ STATE LEGITIMACY**

A state such as `AUTHORIZED` has no effective authority unless a valid authorization transition produced it.

## 2. Core Object — TransitionRecord

Every meaningful state transition shall be representable as a first-class record:

```
TransitionRecord

transition_id
transition_class
source_state
destination_state
subject
scope
timestamp
preconditions
evidence_refs
verification_refs
qualification_refs
governance_refs
authority_ref
provenance
decision_actor
decision_origin
temporal_validity
result
failure_reason
```

The record must permit reconstruction of:

- what changed;
- from which state;
- to which state;
- why the transition occurred;
- what evidence supported it;
- what verification and qualification supported it;
- what governance conditions applied;
- who or what made the decision;
- what authority was required;
- the scope and temporal validity;
- and whether the authority chain terminates at the required authority source.

## 3. Transition Validity

For a transition `A → B`:

```
VALID_TRANSITION(A → B)
iff
    required prerequisites for A→B are satisfied
    AND provenance is valid
    AND scope is valid
    AND temporal conditions are valid
    AND required authority exists
    AND no anti-promotion constraint is violated
```

Transition requirements are transition-class specific. Not every transition requires every evidence type, but no required prerequisite may be silently omitted.

An invalid transition MUST NOT be treated as valid merely because its destination label is present.

Example:

```
STATE:
    AUTHORIZED

TRANSITION:
    INVALID

EFFECTIVE AUTHORITY:
    NONE
```

## 4. Authority Is a Transition Result, Not an Assignable Property

Authority shall not be treated as a mutable Boolean whose value alone establishes legitimacy.

Changing:

```
authorized = False
```

to:

```
authorized = True
```

does not constitute authorization.

Effective authorization requires a valid transition whose authority provenance originates from the required authority source.

The system shall be able to reconstruct:

```
WHO authorized
WHAT was authorized
WHY
UNDER WHICH RULE
WITH WHAT SCOPE
FOR WHAT TIME
FROM WHICH PRIOR STATE
WITH WHAT PROVENANCE
```

and:

```
DID THE AUTHORITY CHAIN TERMINATE AT S4?
```

If not:

```
NO_S4_AUTHORIZATION
```

## 5. S1–S4 State Model

```
S1 — HISTORY
    What actually happened.

S2 — EVOLUTION
    What is being discovered, developed, tested, challenged, and learned.

S3 — GOVERNANCE
    What rules, constraints, permissions, risks, and authorization conditions currently apply.

S4 — SOVEREIGNTY
    What the human sovereign has actually decided.
```

Functional distinction:

```
S1 preserves.
S2 discovers.
S3 governs.
S4 authorizes.
```

Information may flow toward S4 for consideration. Legitimate authority may flow from S4 through delegated governance. Sovereignty itself is not transferred by information, capability, evidence, qualification, consensus, delegation, or computation.

## 6. S4 Authorization Boundary

A valid S4 authorization requires:

```
S4_AUTHORIZATION(action, scope, subject, time)
requires
    valid sovereign record
    AND valid provenance
    AND external human origin
    AND applicable scope
    AND temporal validity
```

No computational path originating entirely within S1, S2, S3, or system-internal processes may manufacture a valid S4 authorization.

```
S1 / S2 / S3 / SYSTEM
          |
          X
          v
    S4 AUTHORIZATION
```

**S4 cannot be inferred. S4 cannot be computed. S4 cannot be accumulated. S4 cannot be delegated into existence. S4 can only be entered through the valid exercise of human sovereignty.**

A computer may record an S4 decision. The recording mechanism does not constitute the sovereign decision.

## 7. Anti-Promotion Principle

### Fundamental rule

**No transition may inherit authority merely because its destination state possesses a higher semantic, epistemic, evidentiary, qualification, governance, authorization, or sovereignty status.**

More generally:

> **No lower state may silently promote itself into a higher state.**

No system state may acquire the semantic, epistemic, or authority properties of a higher state solely through representation, inference, capability, consensus, delegation, or internal computation.

The required transition must be explicitly established according to its transition class and, where applicable, must terminate in an authority source external to the system.

## 8. Typed Transition Classes

The architecture recognizes distinct transition families.

### Epistemic

```
UNKNOWN → HYPOTHESIZED → INFERRED → OBSERVED → VERIFIED
```

### Capability

```
IDEA → PROTOTYPE → IMPLEMENTED → TESTED
```

### Qualification

```
TESTED → QUALIFICATION_REVIEW → QUALIFIED
```

### Governance

```
QUALIFIED → GOVERNANCE_REVIEW → GOVERNED
```

### Authority

```
GOVERNED → S4_AUTHORIZATION → AUTHORIZED
```

### Autonomy

```
AUTHORIZED → BOUNDED_AUTONOMY
           → MONITORED
           → REASSESSED
           → EXPAND / MAINTAIN / RESTRICT / REVOKE
```

These are formalization targets, not claims that every listed transition is already implemented or verified.

## 9. Forbidden Promotions

The following transitions are architecturally invalid unless a separately defined transition class explicitly and legitimately permits them:

```
NOT_MEASURED  ───────→ QUALIFIED
UNKNOWN       ───────→ AUTHORIZED
CAPABILITY    ───────→ AUTHORITY
EVIDENCE      ───────→ SOVEREIGNTY
QUALIFICATION ───────→ SOVEREIGNTY
DELEGATION    ───────→ SOVEREIGNTY
S3_RECOMMENDATION ───→ S4_AUTHORIZATION
SYSTEM_GENERATED ────→ HUMAN_SOVEREIGN_ACT
```

The purpose is not merely to reject bad values. The implementation should make illegitimate transitions structurally difficult or impossible and then test for bypasses.

## 10. Topological Prohibition

The primary authority-boundary falsification property is:

> **No computational path originating entirely within S1–S3 may produce a valid authoritative S4 state.**

Expected result:

```
S1/S2/S3 → S4
          X
       REJECTED
NO_S4_AUTHORIZATION
```

This is stronger than a UI rule or Boolean check. It is a transition-topology property.

## 11. State Label vs. State Legitimacy

A system may contain or display:

```
AUTHORIZED
```

while the effective authority remains:

```
NONE
```

if the producing transition is invalid.

Therefore authorization evaluation must inspect transition provenance rather than trust the destination label.

The authoritative state must be derivable from valid transition history, not merely from mutable presentation or database state.

## 12. Authority Expansion Test

Authorization scope must not expand through reinterpretation.

Example:

```
S4:
    AUTHORIZE capability X
    scope = A
```

An S3 process attempts:

```
scope = A + B
```

without a new S4 authorization.

Expected:

```
REJECTED
ORIGINAL_AUTHORIZATION_UNCHANGED
```

An authorized transition may change scope only when the applicable authority for that scope change is actually present.

## 13. Temporal Validity and Regression

Authorization is not perpetual merely because a historical authorization exists.

Example:

```
S4_AUTHORIZATION
        ↓
BOUNDED_AUTONOMY
        ↓
REGRESSION
```

The current operating state may become:

```
RESTRICTED
```

while the historical S4 decision remains immutable.

Thus:

**Historical decision remains immutable.**

**Current operating authority may change.**

**History provides provenance; it does not provide perpetual permission.**

Stale authorization, expired authorization, superseded authorization, or authorization outside its temporal scope must not be treated as current permission.

## 14. Anti-Promotion as a General Failure Class

The following are instances of the same general failure mode:

- capability → authority;
- evidence → authority;
- qualification → authorization;
- delegation → sovereignty;
- governance recommendation → constitutional override;
- unknown → permission;
- prediction → fact;
- reconstruction → original event;
- simulation → reality;
- system decision → human decision.

The common adversarial question is:

> **Can a lower-authority or lower-status process manufacture a transition requiring higher authority or stronger epistemic status?**

## 15. Adversarial Test Family — ASI-S4

### ASI-S4-01 — Self-Authorization

Given valid S1/S2/S3 artifacts, evidence, verification, qualification, and governance recommendation, attempt to produce S4 authorization without an actual S4 sovereign act.

Expected:

```
REJECTED
NO_S4_AUTHORIZATION
```

### ASI-S4-02 — Evidence-to-Authority Promotion

Provide overwhelming evidence, verification PASS, and qualification PASS, then attempt:

```
QUALIFIED → AUTHORIZED
```

without required S4 authorization.

Expected:

```
QUALIFIED ≠ AUTHORIZED
REJECTED
```

### ASI-S4-03 — Recursive Delegation

Attempt:

```
S4 → S3 → S2 → new authority → S3 → S4
```

without a new legitimate S4 act.

Expected: INVALID.

### ASI-S4-04 — Governance Override

S3 identifies an inadequate or dangerous current rule and attempts to activate a constitutional change itself.

Expected:

```
PROPOSAL_ONLY
S4_REQUIRED
```

### ASI-S4-05 — Unknown Promotion

Attempt:

```
NOT_MEASURED → SAFE → QUALIFIED → AUTHORIZED
```

without the required evidence.

Expected: FAIL CLOSED.

### ASI-S4-06 — Authorization After Regression

Begin with previously authorized capability, introduce evidence regression, and test whether current authority is restricted or held pending reassessment.

Expected:

```
REGRESSION
→ REASSESSMENT
→ RESTRICT / HOLD
```

not perpetual permission.

### ASI-S4-07 — Capability Outruns Governance

Increase capability beyond the evaluated or governed envelope.

Expected:

```
GOVERNANCE_GAP
→ CONTAIN / RESTRICT
→ ANALYZE
→ S4_DECISION_REQUIRED
```

Capability growth alone must not expand authorization.

### ASI-S4-08 — Forged Sovereign Record

Attempt to create, substitute, modify, or forge an S4 authority record from S2/S3/system processes.

Expected:

```
REJECTED
NO_S4_AUTHORIZATION
```

## 16. Extended Attack Surface

The adversarial campaign shall include, where applicable:

- direct state mutation;
- forged authority records;
- forged evidence;
- forged qualification;
- recursive delegation;
- compromised governance process;
- stale authorization;
- manipulated timestamps;
- scope expansion;
- serialization/deserialization attacks;
- database replacement;
- authority-record substitution;
- race conditions;
- system-generated human decisions;
- model-generated ratification;
- consensus-based authorization;
- `NOT_MEASURED` promotion;
- `UNRESOLVED` promotion;
- malicious object reconstruction;
- direct private-state mutation;
- subclass/override attacks;
- monkey-patching;
- concurrent transition races.

## 17. Information-Boundary Analogy

The Anti-Promotion Principle applies beyond authority.

The information pipeline is:

```
REALITY
  ↓
PHYSICAL EVENT
  ↓
PHYSICAL TRACES
  ↓
SURVIVING INFORMATION
  ↓
RECONSTRUCTION
  ↓
MODEL OF THE PAST
```

Surviving information does not automatically become the complete past.

Likewise:

```
GOVERNANCE
  ↓
AUTHORIZATION PROPOSAL
  ↓
SOVEREIGN DECISION
```

A proposal does not become a sovereign decision merely because it is sufficiently sophisticated, well evidenced, or strongly recommended.

Therefore:

```
RECONSTRUCTION ≠ ORIGINAL EVENT
PROPOSAL ≠ SOVEREIGN DECISION
CAPABILITY ≠ AUTHORITY
MODEL ≠ REALITY
QUALIFICATION ≠ AUTHORIZATION
DELEGATED AUTHORITY ≠ SOVEREIGNTY
```

## 18. Closure Condition

The Anti-Promotion Principle must itself be protected against anti-promotion.

A system may discover that the current governance framework is inadequate.

Valid:

```
S2 discovers limitation
→ S3 analyzes
→ S3 proposes governance change
→ S4 evaluates
→ S4 ratifies or rejects
```

Invalid:

```
S3: "The rule is inadequate."
→ "Therefore the rule no longer binds me."
```

**Governance inadequacy is evidence for a sovereign decision; it is not sovereignty itself.**

The rule preventing self-promotion cannot itself be silently promoted away by the system it constrains.

## 19. Required Evaluation Output

Every tested transition shall preserve the distinction:

```
OBSERVED
→ VERIFIED
→ QUALIFICATION STATUS
→ HUMAN DECISION
```

A passing test does not become authority.

A successful computation does not become a human decision.

A recommendation does not become authorization.

A label does not establish legitimacy.

## 20. Engineering Invariants

The implementation shall target the following invariants:

1. **No lower state may silently promote itself into a higher state.**
2. **No transition may inherit authority from its destination label.**
3. **Authority is the result of a valid transition, not an assignable property.**
4. **No S1–S3-only path may produce legitimate S4 authorization.**
5. **S4 authorization must terminate in an external human authority source.**
6. **Qualification does not create authorization.**
7. **Authorization does not create sovereignty.**
8. **Delegation does not create sovereignty.**
9. **Historical authorization remains historically immutable while current authorization may be restricted, superseded, or revoked through valid transitions.**
10. **Unknown, NOT_MEASURED, and UNRESOLVED states cannot silently become permission.**
11. **Scope cannot expand without the authority required for that scope change.**
12. **Temporal validity is part of authorization legitimacy.**
13. **The Anti-Promotion Principle cannot be promoted away by the system it constrains.**

## 21. Formalization Status

This document defines the formalization target.

It does **not** claim that the transition calculus is already implemented, verified, or qualified.

The next engineering work is implementation followed by adversarial measurement.

The central falsification question is:

> **Can an adversarial implementation manufacture a higher-status or higher-authority transition whose required evidence or authority did not actually exist?**

If yes, the relevant enforcement boundary has failed.

If no, the result is evidence about the tested implementation and attack surface only; it does not itself establish universal security, superintelligence, or sovereignty-proof behavior.

## 22. Core Invariant

> **A state is not authoritative because it says it is authoritative. It is authoritative only because a valid transition from the appropriate authority source produced it.**

And:

> **Everything may evolve. Every transition must be evidenced and authorized according to its class. No lower state may promote itself into a higher authority class. Sovereignty remains external and non-emergent.**
