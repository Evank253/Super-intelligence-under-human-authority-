# FORENSIC-001 — RECOVERY MANIFEST

Status: **DISCOVERY PASS 001 — INITIAL SOURCE INVENTORY**
Authority: **NOT YET AUTHORITATIVE**
Source repositories: **READ-ONLY / NOT MODIFIED**
Canonical target: `Evank253/Super-intelligence-under-human-authority-`
Canonical baseline inspected at commit: `b7723bf5b31f97b56eb45235f66e3bf6badb184a`
Canonical baseline tree: `b530c0ac6334af431505919b9ece707ebcd3ec84`
Recovery date: 2026-10-05

## Purpose

This manifest records what was actually located during Forensic Operation 001.

It is a discovery artifact, not a qualification artifact.

No entry below implies that the referenced system, capability, test, metric, or authority path is verified or qualified.

## Forensic rules

1. Repository/artifact identity precedes evaluation.
2. Source repositories are not modified during discovery.
3. A repository name is not sufficient identity; commit/tree/artifact identity must be recorded where available.
4. A copied/imported artifact does not inherit qualification.
5. Historical claims remain historical until their underlying evidence is located and reconciled.
6. Conflicts are recorded rather than silently resolved.
7. Missing evidence is recorded as OPEN / NOT MEASURED.
8. The canonical repository is the reconciliation target, not retroactive proof of source claims.

## Initial discovered source set

| REC ID | Type | System | Source | Ref / Commit | Tree | Artifact / Scope | Discovery status | Qualification |
|---|---|---|---|---|---|---|---|---|
| REC-001 | repository | Super Intelligence Under Human Authority | `Evank253/Super-intelligence-under-human-authority-` | `b7723bf5b31f97b56eb45235f66e3bf6badb184a` | `b530c0ac6334af431505919b9ece707ebcd3ec84` | Canonical integration/reconciliation target | LOCATED / IDENTIFIED | NOT ASSESSED |
| REC-002 | repository | KCN | `Evank253/KCN-SUPER-COGNITIVE-HUMAN-GOVERNED-INTELLIGENCE-ECOSYSTEM-` | `cf8ca49b872a9baaa7212caba28837f486d54062` | `8577031ff35985231c56ec8e46887db2163e34cc` | Large KCN implementation; governance, intelligence, execution, security, verification, tests | LOCATED / IDENTIFIED | NOT ASSESSED |
| REC-003 | repository | MANIFEX | `Evank253/MANIFEX` | `00a41ce1a21cfa58dbf33f29a7a9d600fd34a5ad` | `5db3dbe019986487368447bd2f3a3524a78952ad` | Current MANIFEX source; ER-v2 requirements added in latest commit | LOCATED / IDENTIFIED | NOT ASSESSED |
| REC-004 | repository | MANIFEX Engineering OS | `Evank253/MANIFEX-ENGINEERING-OS` | `c7a19803b732fc8fe8abf29a8f46daec869585a5` | `4e67107cb925bac067039569de79d5ec1bc1f54d` | Capability registry / architecture capture | LOCATED / IDENTIFIED | NOT ASSESSED |
| REC-005 | repository | MANIFEX Engineering-to-Evidence | `Evank253/MANIFEX-ENGINEERING-TO-EVIDENCE` | `2b1e0ec5e365a9b4dae8978221796edb95729623` | `83967b1659824f6e29c159bb5f4665f772a1337b` | Clone-based engineering-to-evidence pipeline | LOCATED / IDENTIFIED | NOT ASSESSED |
| REC-006 | repository | KSI | `Evank253/Ketchums-Super-Intelligence-KSI-` | default branch `Python-3` | PENDING COMMIT RESOLUTION | Prior KSI implementation; kernel/root_control/safety/specs/evals present | LOCATED | NOT ASSESSED |
| REC-007 | repository | KSI Benchmark Suite | `Evank253/KSI-Benchmark-Suite` | default branch `Python-3` | PENDING COMMIT RESOLUTION | benchmark, grader, MLOps/replacement policy infrastructure | LOCATED | NOT ASSESSED |
| REC-008 | repository | Global Intelligence | `Evank253/Global-Intelligence` | default branch `Python-3` | PENDING COMMIT RESOLUTION | Large intelligence/capability repository; KCN architecture, certification/evaluation, tests, strategic future and other domains | LOCATED | NOT ASSESSED |
| REC-009 | repository | KCN-II | `Evank253/KCN-II` | default branch `main` | PENDING COMMIT RESOLUTION | Separate KCN-II implementation/repository | LOCATED | NOT ASSESSED |
| REC-010 | repository | KCN AGSI/ASI | `Evank253/KCN-AGSI-ASI` | default branch `Python-3` | PENDING COMMIT RESOLUTION | Repository located; specific KSI-ASI-001 artifact not established by current search | LOCATED / ARTIFACT GAP | NOT ASSESSED |
| REC-011 | repository | Quantara | `Evank253/ketchums-quantum-physics-labs-by-quantara` | default branch `main` | PENDING COMMIT RESOLUTION | Quantara research/application source located; further identity/evidence mapping required | LOCATED | NOT ASSESSED |
| REC-012 | repository | Quantara Core | `Evank253/Quantara-Core` | default branch `Products` | PENDING COMMIT RESOLUTION | Separate Quantara core repository | LOCATED | NOT ASSESSED |

## Canonical repository artifacts already present

The canonical target was found to contain explicit architecture/provenance controls, including:

- `architecture/system_registry.yaml`
- `architecture/cross_repository_ids.yaml`
- `architecture/evidence_states.yaml`
- `architecture/state-machine.md`
- `architecture/capability_registry.yaml`
- `architecture/authority-boundaries.yaml`
- `architecture/authority-boundaries.md`
- `architecture/capability-evidence-authority.md`
- `specifications/KSI-ASI-001.md`
- `specifications/authorization-model.md`
- `specifications/transition-rules.md`
- `specifications/TRANSITION-CALCULUS-ANTI-PROMOTION.md`
- `specifications/TRANSITION-VALIDITY-SCHEMA.md`
- `evaluation/asi_qualification.py`
- `evaluation/smoke.py`
- `adversarial/ASI-01-self-authority` through `ASI-10-recursive-challenge`
- `provenance/import-manifest/IMPORT-MANIFEST.md`
- `evidence_archive/`
- `legacy/KCN`
- `legacy/KSI`
- `legacy/MANIFEX`
- `legacy/KSI-Benchmark-Suite`

Important current canonical finding:

`architecture/state-machine.md` explicitly says the exact ratified E0-E5 definitions must be recovered from the authoritative source artifact and marks source recovery **OPEN**. Therefore the existence of an E0-E5 description in conversation history is not being promoted to canonical executable semantics.

## Existing import-manifest reconciliation evidence

The pre-existing canonical import manifest already records several source relationships, including:

- MANIFEX `e7660b8f6342f2de0c407a6dc1ea66a782b0b3fe`
- KSI Benchmark Suite `aef8a1ea28739a9d01a332993990e8e370aa3bb6`
- MANIFEX-ENGINEERING-TO-EVIDENCE `2b1e0ec5e365a9b4dae8978221796edb95729623`
- MANIFEX-ENGINEERING-OS `c7a19803b732fc8fe8abf29a8f46daec869585a5`
- KCN `cf8ca49b872a9baaa7212caba28837f486d54062`
- KSI `91360e7e146f8b870098c30f0fed38ea484ba3a3`
- KCN-AGSI-ASI: repository located; specific KSI-ASI-001 artifact not found by that audit

The existing manifest explicitly states that these source hashes identify retrieved artifacts and **do not certify the claims contained within them**.

## Recovered-claim quarantine

The following remain claims requiring source/evidence reconciliation:

- KCN 12 modules / 11 tools / 8 tests
- KCN v3 99.88% / 7,000-run result / 9.6269 ms latency
- historical Omni-Matrix 21M tests / 99.69% pass / 0.00095% hallucination
- MANIFEX approximately 1,076-file inventory
- KAP 99.8% metric
- TEVV-002 10,000 rows / 8 workers / concurrency 32 / p50 357 ms / p95 665 ms / p99 693 ms
- historical ARENA 67 PASS / 2 NOT MEASURED / 0 FAIL
- F-T11a, T4b, T13, and T2/B08-H1 failure lineage
- FIE-001 empirical measurement status
- QUANTARA scientific validation status

These claims are preserved but are **not promoted by this manifest**.

## Next forensic operations

1. Resolve commit/tree identity for remaining located repositories.
2. Enumerate repository branches/tags relevant to historical states.
3. Enumerate exact artifacts inside each source repository.
4. Reconcile canonical imports against current source identities.
5. Build `FORENSIC-001-ENTITY-REGISTRY`.
6. Build `FORENSIC-001-CLAIM-REGISTRY`.
7. Build `FORENSIC-001-CONFLICT-REGISTRY`.
8. Only then construct the full System-of-Systems Recovery & Qualification Map.

## Explicit non-claim

This manifest does **not** establish:

- system-wide integration,
- system-wide verification,
- qualification,
- authorization,
- independent verification,
- production readiness,
- correctness of historical benchmark claims.

It establishes only that the listed source locations and, where recorded, their exact Git identities were located during this discovery pass.
