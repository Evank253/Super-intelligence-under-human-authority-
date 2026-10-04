# Traceability & Recovery Engine — Architectural Requirement v1

**Status:** ARCHITECTURAL REQUIREMENT  
**Scope:** Evaluation / Traceability layer  
**Authority:** This document defines an engineering/epistemic constraint. It does not create qualification, authorization, or S4 authority.

## Purpose

The Traceability & Recovery Engine prevents two classes of system failure:

1. unsupported knowledge generation when required information is missing; and
2. unnecessary reconstruction when prior work already exists elsewhere in the recoverable system history.

It operates across current and historical repositories, commits, trees, files, modules, components, capabilities, implementations, tests, runs, observations, scores, evidence, dependencies, and related artifacts.

## Canonical principles

- **TRACE BEFORE CLAIM** — establish provenance before asserting where information came from.
- **TRACE BEFORE BUILD** — search existing and historical work before proposing new implementation.
- **RECOVER BEFORE REBUILD** — when prior work is found, reconstruct and assess it before recreating it.
- **PRESERVE THE GAP BEFORE FILLING IT** — when required information cannot be established, preserve the gap rather than inventing a bridge.
- **ABSENCE REQUIRES EVIDENCE** — failure to locate an object within one context is not evidence that the object never existed.

## Core invariants

### 1. No False Absence

Failure to locate an implementation, capability, artifact, evidence item, or prior work in the current working context shall not be represented as proof that it does not exist.

`SEARCH_EXHAUSTED_FOR_SCOPE != DOES_NOT_EXIST`

A stronger absence claim requires evidence appropriate to the claim.

### 2. Missing-Information Preservation

When a required dependency cannot be established, the engine shall create or retain an explicit missing/unresolved finding rather than silently replacing the dependency with inference, assumption, generated content, or unsupported provenance.

### 3. Prior-Work Preservation

Before proposing creation, replacement, or reconstruction of a capability, the engine shall perform an appropriately scoped trace for existing, historical, superseded, partial, renamed, moved, or related implementations and evidence.

### 4. Historical Existence Is Not Current Validity

Recovering prior work establishes that the work existed at the identified provenance point. It does not by itself establish that the work is currently valid, verified, qualified, governed, or authorized.

### 5. Recursive Dependency Recovery

A discovered artifact may expose additional required information. The engine shall recursively trace those dependencies and preserve newly discovered gaps.

### 6. No Unsupported Bridge

The engine shall not convert:

- UNKNOWN → CLAIM
- MISSING → FABRICATED EVIDENCE
- NOT FOUND → DOES NOT EXIST
- PRIOR WORK NOT FOUND → BUILD FROM ZERO
- HISTORICAL IMPLEMENTATION → CURRENTLY VALID

### 7. No Authority Creation

The Traceability & Recovery Engine may discover, reconstruct, diagnose, and report. It shall not convert:

- EVIDENCE → AUTHORITY
- TRACEABILITY → QUALIFICATION
- DISCOVERY → AUTHORIZATION
- RECOVERY → HUMAN RATIFICATION

Human/governance layers retain decisions concerning reuse, qualification, scope, deployment, authorization, and final authority.

## Core operating loop

```text
REQUEST / CLAIM
      |
      v
TRACEABILITY
      |
      +--> EXISTING WORK
      |       |
      |       v
      |   RECONSTRUCT LINEAGE
      |       |
      |       v
      |   DETERMINE CURRENT STATE
      |
      +--> NOT FOUND HERE
              |
              v
        SEARCH BROADER TRACE SCOPE
              |
          +---+---+
          |       |
        FOUND   NOT FOUND
          |       |
          v       v
       RECOVER  MISSING
                  |
                  v
          PRESERVE GAP
                  |
                  v
           TRACE IMPACT
                  |
          +-------+-------+
          |               |
       ESTABLISHED     UNRESOLVED
          |               |
          v               v
   CONTINUE/ADAPT    DO NOT INFER
   /REPAIR/REUSE
```

## Recursive evidence-debt example

```text
Capability
  ↓
Implementation FOUND
  ↓
Test FOUND
  ↓
Test references Evidence A
  ↓
Evidence A FOUND
  ↓
Evidence A requires Artifact B
  ↓
Artifact B MISSING
  ↓
Artifact B requires Dataset C
  ↓
Dataset C MISSING
```

The correct result is not to rebuild the implementation. The engine reports that the implementation was recovered and that B and C are the current traceability/evidence bottlenecks.

## Capability family

- **MIL-001 — Missing Information Locator**
  Identifies information required to establish a claim, provenance chain, implementation state, test result, or evidence relationship that cannot currently be established.

- **TPP-001 — Prior-Work Preservation**
  Requires appropriately scoped prior-work search before duplicative construction.

- **NFA-001 — No False Absence**
  Prevents local non-discovery from being represented as global non-existence.

- **RCR-001 — Recursive Dependency Recovery**
  Follows dependencies discovered while tracing another dependency.

- **LCR-001 — Lineage Continuity & Recovery**
  Reconstructs source → version → artifact → implementation → capability lineage where evidence permits.

- **DUP-001 — Duplicate-Work Detection**
  Identifies existing or overlapping implementations before new construction.

- **EGB-001 — Evidence-Gap Blocking**
  Preserves required evidence gaps and prevents unsupported provenance or evidentiary inference.

- **RCR-002 — Traceability Debt Detection**
  Identifies recovered prior work whose lineage, tests, raw evidence, or current-state evidence remains incomplete.

## Required result distinctions

The engine shall distinguish at minimum:

- FOUND
- RECOVERED
- SEARCH_EXHAUSTED_FOR_SCOPE
- MISSING
- UNRESOLVED
- CONFLICTING
- SUPERSEDED
- IMPLEMENTED_UNMEASURED
- EVIDENCE_GAP
- TRACEABILITY_DEBT

These states describe traceability/epistemic conditions. They do not create authority.

## Human/governance boundary

When prior work is found, the engine may report:

> Existing implementation recovered. Provenance and current state are shown below. The implementation appears relevant, but reuse/qualification/authorization remains a separate decision.

When required information is missing, the engine may report:

> Required information is missing or unresolved. The evidence chain is incomplete. No unsupported substitute has been accepted.

The engine must not independently authorize reuse or promote a recovered artifact to qualification or S4 authority.

## Relationship to the Evaluation Ledger

The Traceability & Recovery Engine operates across the ledger topology:

```text
Source
 → Commit / Tree
 → File
 → Module
 → Component
 → Capability
 → Implementation
 → Test
 → Test Run
 → Observation
 → Score
 → Evidence
 → Verification
 → Qualification
 → Governance
 → Human Decision
```

It also traces lateral relationships including dependencies, composition, complementarity, duplication, contradiction, supersession, and bottlenecks.

## Engineering objective

The engine exists to reduce:

- AI hallucinated provenance
- unsupported claims
- false absence claims
- duplicated engineering
- rebuilding of recoverable work
- fragmented capability lineage
- repeated experiments
- lost evidence
- unnecessary compute
- unnecessary human labor

while preserving the separation between discovery, evidence, qualification, governance, and human authority.

## Canonical statement

> **Traceability is a prerequisite to asserting absence, generating unsupported knowledge, or initiating duplicative engineering work.**
