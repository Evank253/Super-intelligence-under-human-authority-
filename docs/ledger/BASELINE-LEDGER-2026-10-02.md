# Baseline Ledger — Current State Snapshot

**Record type:** Dated current-state ledger (documentation of observed state only)
**Date:** 2026-10-02 (America/Los_Angeles)
**Recorded by:** Independent reconstruction from repository commits and files
**Status:** ADOPTED as documentation of observed state
**Claim promotion:** NONE — this ledger does not promote any claim

## Purpose

Freeze a dated snapshot of the project's actual state as reconstructed from
repository evidence, so that subsequent work can be compared against a
recorded baseline rather than narrative summaries.

Missing evidence remains NOT MEASURED / NOT ESTABLISHED. It is never
silently converted into a positive result.

## Governing sequence (unchanged)

Architecture → Human Ratification → Implementation Authorization →
Implementation → Independent Verification → Qualification → Human Ratification

## Ledger

| Component | Repository | Ref / commit | Status |
|-----------|------------|--------------|--------|
| Canonical SoS repo | `Evank253/Super-intelligence-under-human-authority-` | branch `Python-3`, HEAD `b6d3c4f7cc3da9ef0f06d261240a3bda82463813` | Architecture foundation / integration audit |
| IP/provenance baseline | same | `01c0d11b86113f48c5aa1e2c5b91362b22a812e6` | Repository-control baseline; not architecture verification |
| SOS-ARCH-001 | `docs/architecture/SOS-ARCH-001-SYSTEM-OF-SYSTEMS.md` | added in `b6d3c4f7` | PROPOSED — not human-ratified; implementation NOT AUTHORIZED |
| STATUS.md | repo root | `e20a0389…` | Verification status: NOT ESTABLISHED |
| BASELINE.md | repo root | `a3482c93…` | Repository-control baseline record |
| Constitution artifacts | `CONSTITUTION.md`, `constitution/*` | present | IMPLEMENTED as docs/YAML artifacts; runtime enforcement NOT MEASURED in this pass |
| Verification gates | `verification/state_transitions/gates.py` | present | IMPLEMENTED as code artifact; full authority-boundary campaign NOT MEASURED |
| Adversarial harness | `adversarial/blind-harness/` | present | Code present; campaign results NOT MEASURED in this pass |
| Legacy KCN/KSI/MANIFEX | `legacy/*` | snapshots | Historical/recoverable; import status must be established individually |
| TS-ARCH-001 Historical | `Evank253/KSI-EMERGENT-INTELLIGENCE` | `e8c3e572da76f79a94328200a21cac8a4ebaf4bb` | FROZEN HISTORICAL BASELINE |
| TS-ARCH-001 Rev1 | same | `b37c2e69915e9724dcd097304606fce498fbd9a8` | Successor architecture text in tree; human ratification NOT YET GRANTED; implementation NOT AUTHORIZED |
| TS-002 | `docs/milestones/TS-002-…md` | `a252ae214beac505127a0ba7ba0a35d754cf8988` (draft); current tree `792d0ab2…` | DRAFT — prior adversarial review: REVISION REQUIRED; not implementation |
| TS-CON-001 | — | — | NOT STARTED |
| RUNNER-GOV-002 | Runner lineage (KSI-EMERGENT) | Eval 002 evidence | ESTABLISHED under evaluated designed public scope (unauthorized execution prevented when instrumented); private-attribute residual is a known limitation |
| Runner v0.1.1 boundary consolidation | KSI-EMERGENT | `bfd004e3…`, `c159137d…` | IMPLEMENTED; independently evaluated (Eval 003) |
| RUNNER-GOV-003 | `docs/milestones/RUNNER-GOV-003-CAPABILITY-CONSTRAINED-EXECUTION.md` | ratified in `940e62408df0f08f39451b32c9829ce4064247af` | Specification RATIFIED; implementation NOT AUTHORIZED |
| M02 | referenced across docs; `runner/integrations/m02.py` raises NotImplementedError | — | Role defined as independent measurement; live independence NOT MEASURED in this pass |
| Kronos | `runner/integrations/kronos.py` raises NotImplementedError | — | NOT CONNECTED |
| MANIFEX / KCN / KSI ecosystems | separate repos + legacy snapshots | various | Historical/recoverable; import/qualification must be established individually |

## Non-claims (explicit)

This ledger does not establish:

- implementation of any architecture;
- verification or qualification of any claim;
- human ratification of TS-ARCH-001 Rev1 or SOS-ARCH-001;
- GOV-003 implementation;
- any live bridge;
- M02 independence;
- production security, formal verification, or general AI safety.

## Provenance

- Reconstruction performed by independent inspection of repository commits and
  file contents on 2026-10-02.
- No historical artifact was modified by this record.
- No claim was promoted by this record.
