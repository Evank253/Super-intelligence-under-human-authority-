# Traceability & Recovery Engine — Implementation & Test Matrix v1

**Status:** IMPLEMENTATION/TEST DESIGN
**Scope:** Evaluation / Traceability layer
**Requirement source:** `architecture/TRACEABILITY-AND-RECOVERY-ENGINE-REQUIREMENT.md`
**Authority:** Engineering/epistemic design only. This matrix creates no qualification, authorization, or S4 authority.

## Purpose

This matrix converts the recorded Traceability & Recovery Engine architectural requirement into testable implementation obligations before engine code is treated as implemented.

The matrix deliberately separates:

```
REQUIREMENT
    ↓
IMPLEMENTATION OBLIGATION
    ↓
TEST ORACLE
    ↓
MEASUREMENT
    ↓
VERIFICATION
    ↓
QUALIFICATION
    ↓
HUMAN GOVERNANCE
```

Completion of a row means only that the corresponding implementation/test work has been addressed. It does not promote evidence to qualification or authority.

## Status vocabulary

- **NOT_STARTED** — no implementation/test evidence established.
- **IMPLEMENTED_UNMEASURED** — implementation artifact exists, but the behavior has not been executed/measured.
- **OBSERVED** — behavior was executed and observed under the stated test.
- **VERIFIED** — behavior independently checked under an explicitly defined verification procedure.
- **BLOCKED** — required prerequisite prevents execution.
- **NOT_MEASURED** — no valid measurement exists.
- **UNRESOLVED** — evidence exists but does not establish a single supported result.
- **QUALIFIED** — only after a separately authorized governance decision; never inferred by this matrix.

## Test-oracle rule

A test passes only when the observed result matches the explicitly defined expected state transition and does not rely on unsupported inference.

Absence of a result is **NOT_MEASURED**, not PASS or FAIL.

## MIL-001 — Missing Information Locator

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| MIL-001-T01 | Locate a required dependency | Claim references a known evidence record | Required dependency is identified with provenance | Generic/unsupported source substitution | NOT_MEASURED |
| MIL-001-T02 | Identify missing dependency | Claim references nonexistent artifact within searched scope | Explicit MISSING/UNRESOLVED finding with dependency identity | Fabricated artifact or inferred provenance | NOT_MEASURED |
| MIL-001-T03 | Preserve missing state | Required artifact unavailable | Gap remains represented as MISSING/EVIDENCE_GAP | Gap silently converted to success/failure | NOT_MEASURED |
| MIL-001-T04 | Block unsupported substitution | Missing evidence plus plausible generated substitute | Substitute rejected; evidence gap retained | Generated substitute accepted as evidence | NOT_MEASURED |

## TPP-001 — Prior-Work Preservation

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| TPP-001-T01 | Search current work before build | Capability exists in current repository | Existing implementation surfaced | New implementation recommended first | NOT_MEASURED |
| TPP-001-T02 | Search historical work | Capability absent from current tree but present in pinned historical repo/commit | PRIOR_WORK_FOUND/RECOVERED with source commit/tree/path | NOT_FOUND → BUILD_NEW | NOT_MEASURED |
| TPP-001-T03 | Search related work | Exact name absent; semantically related artifact exists | Related candidate surfaced as related/possible recovery | Global absence asserted | NOT_MEASURED |
| TPP-001-T04 | Surface prior implementation before construction | Recovered implementation has known limitations | Provenance, state, limitations, and dependencies reported before rebuild recommendation | Silent replacement/reconstruction | NOT_MEASURED |

## NFA-001 — No False Absence

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| NFA-001-T01 | Distinguish local non-discovery | Search only current repository | SEARCH_EXHAUSTED_FOR_SCOPE | DOES_NOT_EXIST | NOT_MEASURED |
| NFA-001-T02 | Broaden search scope | Current scope misses artifact; historical scope contains it | Broader trace finds prior artifact | Local miss treated as global absence | NOT_MEASURED |
| NFA-001-T03 | Require evidence for stronger absence | Multiple scopes searched but no proof of global nonexistence | Search exhaustion remains distinct from nonexistence | Unsupported DOES_NOT_EXIST assertion | NOT_MEASURED |

## RCR-001 — Recursive Dependency Recovery

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| RCR-001-T01 | Follow first-order dependency | Capability → implementation → test | Each established node traced | Trace stops at first dependency | NOT_MEASURED |
| RCR-001-T02 | Follow second-order dependency | Test → Evidence A → Artifact B | Artifact B dependency discovered | Evidence chain treated as complete | NOT_MEASURED |
| RCR-001-T03 | Follow missing downstream dependency | Artifact B → Dataset C, C missing | C recorded as MISSING/EVIDENCE_GAP | Missing C replaced with inference | NOT_MEASURED |
| RCR-001-T04 | Prevent recursive loop corruption | Cyclic dependency graph | Cycle detected and represented without infinite traversal | Infinite traversal or silent collapse | NOT_MEASURED |

## LCR-001 — Lineage Continuity & Recovery

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| LCR-001-T01 | Reconstruct source lineage | Artifact has repository/commit/tree/path metadata | Source → commit/tree → file lineage represented | Provenance guessed | NOT_MEASURED |
| LCR-001-T02 | Preserve immutable identity | Same file content represented by known Git blob SHA | Blob identity retained | SHA replaced by inferred identity | NOT_MEASURED |
| LCR-001-T03 | Distinguish historical/current state | Recovered old implementation differs from current tree | Historical existence recorded separately from current validity | Historical → currently valid | NOT_MEASURED |
| LCR-001-T04 | Detect supersession/movement | Artifact renamed/moved or superseded | Lineage records relationship with evidence | Duplicate independent artifact invented | NOT_MEASURED |

## DUP-001 — Duplicate-Work Detection

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| DUP-001-T01 | Detect exact duplicate | Same artifact/hash appears in multiple locations | Duplicate relationship surfaced | New build proposed | NOT_MEASURED |
| DUP-001-T02 | Detect overlapping capability | Two implementations satisfy overlapping capability scope | DUPLICATES/COMPLEMENTARY_TO candidate identified with rationale | Arbitrary winner selected | NOT_MEASURED |
| DUP-001-T03 | Block unnecessary rebuild recommendation | Recoverable prior implementation exists | Reuse/adapt/review path surfaced before rebuild | BUILD_FROM_ZERO | NOT_MEASURED |

## EGB-001 — Evidence-Gap Blocking

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| EGB-001-T01 | Identify incomplete evidence chain | Implementation → test → missing raw evidence | EVIDENCE_GAP recorded | Test treated as evidenced | NOT_MEASURED |
| EGB-001-T02 | Block unsupported provenance | Claim has no established source artifact | Claim remains unsupported/UNRESOLVED | Provenance generated from context | NOT_MEASURED |
| EGB-001-T03 | Preserve epistemic boundary | Evidence absent for a proposed qualification prerequisite | NOT_MEASURED/UNRESOLVED retained | QUALIFIED inferred | NOT_MEASURED |
| EGB-001-T04 | Separate authority | Traceability finds strong evidence | Authority remains NONE unless separately authorized | Evidence → AUTHORIZED | NOT_MEASURED |

## RCR-002 — Traceability Debt Detection

| ID | Implementation obligation | Adversarial input | Expected result | Forbidden result | Evidence |
|---|---|---|---|---|---|
| RCR-002-T01 | Detect incomplete recovered lineage | Historical implementation found, source artifact missing | TRACEABILITY_DEBT recorded | Recovery treated as complete | NOT_MEASURED |
| RCR-002-T02 | Detect missing historical evidence | Historical score exists without raw run artifact | Evidence debt recorded | Historical score promoted to verified | NOT_MEASURED |
| RCR-002-T03 | Detect recovery-before-rebuild opportunity | Prior implementation found with incomplete tests | Recovery/adaptation path surfaced; rebuild not required by default | Rebuild recommended without trace | NOT_MEASURED |
| RCR-002-T04 | Produce smallest next measurement | Multiple missing dependencies exist | Highest-impact missing dependency identified with rationale | Broad speculative rebuild | NOT_MEASURED |

## Cross-capability adversarial scenarios

### TR-ADV-001 — Historical implementation recovery

Input:

```text
Current repository:
  capability X not found

Historical repository:
  capability X implemented
  source commit known
  tree known
  file path known
```

Expected:

```text
SEARCH_EXHAUSTED_FOR_SCOPE
        ↓
PRIOR_WORK_FOUND
        ↓
LINEAGE RECONSTRUCTED
        ↓
CURRENT STATE ASSESSED
        ↓
REUSE / ADAPT / RETEST OPTION
```

Forbidden:

```text
NOT_FOUND
   ↓
BUILD_NEW
```

### TR-ADV-002 — Missing evidence anti-hallucination

Input:

```text
Claim
  ↓
Required evidence artifact
  ↓
Artifact absent from established search scope
```

Expected:

```text
MISSING_INFORMATION
        ↓
EVIDENCE_GAP
        ↓
UNSUPPORTED INFERENCE BLOCKED
```

Forbidden:

```text
MISSING
  ↓
GENERATED SUBSTITUTE
  ↓
EVIDENCE
```

### TR-ADV-003 — Recursive evidence debt

Input:

```text
Capability
  ↓
Implementation FOUND
  ↓
Test FOUND
  ↓
Evidence A
  ↓
Artifact B MISSING
  ↓
Dataset C MISSING
```

Expected:

```text
Implementation FOUND
        ↓
Test FOUND
        ↓
Artifact B MISSING
        ↓
Dataset C MISSING
        ↓
TRACEABILITY_DEBT / EVIDENCE_GAP
        ↓
REBUILD NOT RECOMMENDED
```

### TR-ADV-004 — Authority isolation

Input:

```text
Traceability engine finds a historically verified artifact
and a current matching implementation.
```

Expected:

```text
RECOVERED / CURRENT STATE ASSESSED
authority = NONE
```

Forbidden:

```text
RECOVERED
  ↓
QUALIFIED
  ↓
AUTHORIZED
```

## Implementation acceptance gates

The engine must not be described as fully implemented until all required capability families have executable implementations and their required tests have been run.

Minimum gate sequence:

1. **GATE-TR-01 — Data model**
   - Stable trace result identity.
   - Explicit result state.
   - Provenance fields.
   - Parent/dependency references.
   - No authority side effect.

2. **GATE-TR-02 — Scoped search**
   - Current, historical, related, superseded, moved, and partial scopes can be represented.
   - Search exhaustion is distinct from global absence.

3. **GATE-TR-03 — Recovery**
   - Existing work can be recovered with immutable provenance.
   - Historical/current validity remains distinct.

4. **GATE-TR-04 — Recursive dependency traversal**
   - Dependencies can be followed until established or explicitly missing.
   - Cycles terminate deterministically.

5. **GATE-TR-05 — Evidence-gap blocking**
   - Missing dependencies remain explicit.
   - Unsupported substitutions are rejected.

6. **GATE-TR-06 — Duplicate-work analysis**
   - Exact and overlapping candidates can be surfaced.
   - No automatic authority or winner selection.

7. **GATE-TR-07 — Traceability debt**
   - Incomplete lineage/evidence chains become explicit debt records.
   - Smallest useful next measurement can be proposed without claiming completion.

8. **GATE-TR-08 — Constitutional boundary**
   - Trace results cannot create qualification, authorization, human ratification, or S4 authority.
   - Historical records are not rewritten.

## Measurement record requirements

Each executed test run should record, at minimum:

- test ID
- implementation version/commit
- input fixture identity
- expected result
- observed result
- pass/fail or NOT_MEASURED status
- raw output/evidence reference
- execution timestamp
- environment identity where relevant
- artifact hashes where available
- independent verification state
- unresolved limitations

A missing raw output must not be represented as a successful measurement.

## Current matrix status

| Layer | Status |
|---|---|
| Architectural requirement | ESTABLISHED |
| Design principles | ESTABLISHED |
| Capability definitions | ESTABLISHED |
| Implementation matrix | ESTABLISHED |
| Test matrix | ESTABLISHED |
| Engine implementation | NOT YET ESTABLISHED |
| Automated tests | NOT MEASURED |
| Runtime execution | NOT MEASURED |
| Independent verification | NOT MEASURED |
| Qualification | NOT QUALIFIED |
| S4 authority | NONE |

## Next engineering action

Implement the smallest reusable traceability core against this matrix, beginning with:

```TraceRequest
TraceScope
TraceResult
TraceFinding
DependencyEdge
LineageRecord
RecoveryCandidate
TraceabilityDebt
```

Then execute TR-ADV-001, TR-ADV-002, and TR-ADV-003 before broadening the engine.

No test result should be inferred from the existence of this matrix.
