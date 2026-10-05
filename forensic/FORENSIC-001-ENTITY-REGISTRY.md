# FORENSIC-001-ENTITY-REGISTRY

**Operation:** FORENSIC-001 — Identity & Reconciliation  
**Pass:** 001 — Entity Identity Resolution  
**Status:** ACTIVE / RECONCILIATION IN PROGRESS  
**Authority:** Forensic working record; NOT a qualification or certification artifact  
**Canonical target repository:** `Evank253/Super-intelligence-under-human-authority-`  
**Forensic branch:** `forensic-001/recovery-manifest`  
**Forensic branch commit before this registry:** `3e6ff22f30632c9c6806ed0ba036f16ff6430ff8`

## 1. Purpose

This registry establishes cryptographic and structural identities for recovered repositories and relevant repository states.

It deliberately distinguishes:

- repository identity from repository state identity;
- current heads from historical imported states;
- commit identity from tree/artifact identity;
- copied artifacts from source artifacts;
- relationship/reconciliation from correctness;
- implementation from verification and qualification.

A repository name is not treated as a sufficient identity.

## 2. Forensic invariants

1. Source/default repositories are not modified by this discovery pass.
2. Historical states remain historical even when later states exist.
3. Current heads do not retroactively replace historical provenance.
4. A matching filename does not establish artifact identity.
5. A copied artifact inherits provenance; it does not inherit qualification.
6. Reconciliation establishes a relationship, not correctness.
7. Conflicting records are retained rather than silently resolved.
8. Qualification and authority are not inferred from repository presence.
9. Missing identity evidence remains OPEN.
10. The canonical repository is a reconciliation target, not retroactive proof of source claims.

## 3. Current repository identity anchors

| Entity | Repository | Ref | Current commit | Current tree | Identity status |
|---|---|---|---|---|---|
| Canonical Super Intelligence | Evank253/Super-intelligence-under-human-authority- | Python-3 | b7723bf5b31f97b56eb45235f66e3bf6badb184a | b530c0ac6334af431505919b9ece707ebcd3ec84 | ESTABLISHED |
| MANIFEX | Evank253/MANIFEX | Python-3 | 00a41ce1a21cfa58dbf33f29a7a9d600fd34a5ad | 5db3dbe019986487368447bd2f3a3524a78952ad | ESTABLISHED |
| MANIFEX Engineering OS | Evank253/MANIFEX-ENGINEERING-OS | Python-3 | c7a19803b732fc8fe8abf29a8f46daec869585a5 | 4e67107cb925bac067039569de79d5ec1bc1f54d | ESTABLISHED |
| MANIFEX Engineering → Evidence | Evank253/MANIFEX-ENGINEERING-TO-EVIDENCE | Python-3 | 2b1e0ec5e365a9b4dae8978221796edb95729623 | 83967b1659824f6e29c159bb5f4665f772a1337b | ESTABLISHED |
| KSI | Evank253/Ketchums-Super-Intelligence-KSI- | Python-3 | 91360e7e146f8b870098c30f0fed38ea484ba3a3 | 88e86f62ed7f445a6ed9c79ed0b6f55781be08e4 | ESTABLISHED |
| KSI Benchmark Suite | Evank253/KSI-Benchmark-Suite | Python-3 | f710816cf0cf0fa1287ee3d4c718b950875d30f4 | a1dfedfe592cea50eed05658f71d52b0e52ba947 | ESTABLISHED |
| Global Intelligence | Evank253/Global-Intelligence | Python-3 | 754fb1ff22da0de58ec4db525f137d09a06ae75a | a41f3497495789222c29ad54758fe14e5a118cce | ESTABLISHED |
| KCN-II | Evank253/KCN-II | main | 5c63cdf57e464813f514794b5e67bcc030b2f225 | 138116ab70bec6b760e78724bbe842315c57b50f | ESTABLISHED |
| KCN AGSI/ASI | Evank253/KCN-AGSI-ASI | Python-3 | 16c3da0d9f131f55685095f5bfd1bcf8b27c18b2 | acce580ca76a0eacd7a3a26c3a0139f15de8625b | ESTABLISHED |
| KCN Super Cognitive Ecosystem | Evank253/KCN-SUPER-COGNITIVE-HUMAN-GOVERNED-INTELLIGENCE-ECOSYSTEM- | copilot/kcn-super-cognitive-ecosystem | cf8ca49b872a9baaa7212caba28837f486d54062 | 8577031ff35985231c56ec8e46887db2163e34cc | ESTABLISHED |
| Quantara Physics Labs | Evank253/ketchums-quantum-physics-labs-by-quantara | main | 4b2d7bfc0f4f4d68af1a957aa28cd6f2cd94a98d | d2fc9224c94531a4c278393a6cb2022e97aa51b6 | ESTABLISHED |
| Quantara Core | Evank253/Quantara-Core | Products | 3e981a860b954329f8a4fc4f44a5b7f0c09ff2c1 | 77f958bf191e9e13064526ab33be907b138d1568 | ESTABLISHED |

## 4. Canonical repository state graph

The canonical repository is explicitly modeled as multiple states.

### Baseline anchor

- Commit: `01c0d11b86113f48c5aa1e2c5b91362b22a812e6`
- Relationship to current Python-3 head: current head is 144 commits ahead.
- Status: historical baseline anchor.

### EA-G1

EA-G1 is established as a **commit series**, not yet as one single immutable release commit in this registry.

Earliest recovered EA-G1 implementation commit:
- `ca0f7c4d1a92962a31fcac46ff208310082ba008` — add `ea_g1/__init__.py`

Additional EA-G1 series commits include the engine, models, schemas, and adversarial specifications.

Status: state family ESTABLISHED; exact terminal EA-G1 state anchor remains OPEN.

### EA-G2/current

- Commit: `b7723bf5b31f97b56eb45235f66e3bf6badb184a`
- Tree: `b530c0ac6334af431505919b9ece707ebcd3ec84`
- Message: Add EA-G2 ASI qualification harness and protocol
- Parent: `0adfc48259c8287900f44882566ce6ce4a7a2294`
- Current Python-3 head: YES

The EA-G2 commit adds `.github/workflows/asi-harness.yml`, which runs the evaluation smoke test and compile check.

**Important:** presence of an EA-G2 qualification harness does not itself establish qualification.

## 5. Forensic branch identity

The discovery branch is:

`refs/heads/forensic-001/recovery-manifest`

Current recorded branch target:
`3e6ff22f30632c9c6806ed0ba036f16ff6430ff8`

The entity registry is being written to this forensic branch only.

## 6. Historical import-state reconciliation

### KSI Benchmark Suite

Historical imported state:
- Commit: `aef8a1ea28739a9d01a332993990e8e370aa3bb6`
- Tree: `6b3343ea70387b384336d7528e18364b9fc8e96b`
- Message: KS Benchmark Suite v1.0 — benchmark runner, replacement policy, web dashboard
- Parent: none
- Role: historical imported source state

Current state:
- Commit: `f710816cf0cf0fa1287ee3d4c718b950875d30f4`
- Tree: `a1dfedfe592cea50eed05658f71d52b0e52ba947`
- Parent: `aef8a1ea28739a9d01a332993990e8e370aa3bb6`
- Role: current repository head

Git comparison establishes:
- current is ahead by exactly 1 commit;
- historical commit is the merge base;
- the only changed file is `Procfile`, added at current state.

Therefore:

`KSI-Benchmark-Suite` repository identity remains one repository, while the historical import state and current state are distinct state nodes.

### MANIFEX

Historical imported state:
- Commit: `e7660b8f6342f2de0c407a6dc1ea66a782b0b3fe`
- Tree: `9d6b827c697623467a3826ca9880bc67af1c3d83`
- Message: Add MANIFEX Build Index asset registry and qualification gate

Current state:
- Commit: `00a41ce1a21cfa58dbf33f29a7a9d600fd34a5ad`
- Tree: `5db3dbe019986487368447bd2f3a3524a78952ad`
- Parent: `3e3722476ec6ee3c5056b7fb62ebcfcf6e628cf6`
- Message: docs: define ER-v2 requirements from Experiment 001

Git comparison establishes:
- current is 13 commits ahead of the historical import state;
- historical state is the merge base;
- current adds ER-v2 requirements and Experiment-001 evidence/integrity records, execution-evidence code, execution-registration code, and associated tests.

This is state evolution, not provenance invalidation.

### KCN Super Cognitive Ecosystem

Established state:
- Commit: `cf8ca49b872a9baaa7212caba28837f486d54062`
- Tree: `8577031ff35985231c56ec8e46887db2163e34cc`
- Branch: `copilot/kcn-super-cognitive-ecosystem`
- Repository default branch: same branch
- Merge commit with two parents:
  - `20090fb834e9271ebf84b40d68b2b932ff120bb4`
  - `e0aadacb557372d25a5dd2d255b19bc3df637047`

This resolves the previous branch-path limitation sufficiently to establish the known current/default identity without fabricating a different head.

Observed relevant branches include numerous Copilot branches; examples include:
- `copilot/kcn-super-cognitive-ecosystem`
- `copilot/kcn-phase-2-sprint-1-backend-foundation`
- `copilot/fix-ci-deployment-issues`
- `copilot/fix-failing-github-actions-job`
- `copilot/fix-github-actions-job-python-3-12`
- `copilot/set-up-branch-protection-rules`
- `copilot/update-landingpage-portal-interface`

Branch enumeration is not yet certified exhaustive.

## 7. Current artifact/file-state observations

### KSI Benchmark Suite

At historical imported state `aef8a1ea...`:
- 17 files.
- Key artifacts include:
  - `README.md`
  - `benchmark/grader.py`
  - `benchmarks/architecture.jsonl`
  - `mlops/replacement_policy.py`
  - `mlops/run_student_benchmark.py`
  - `requirements.txt`
  - `server.py`

At current state `f710816c...`:
- 18 files.
- Same core artifacts plus `Procfile`.

### MANIFEX

At historical import state `e7660b8f...`:
- 2 files identified in the commit tree.
- `README.md`
- `manifex/build_index.py`

At current state `00a41ce1...`:
- 11 files.
- Existing `manifex/build_index.py` remains.
- Added execution-evidence, execution-registration, tests, and Experiment-001 / ER-v2 documentation.

### KCN Super Cognitive Ecosystem

At `cf8ca49...`:
- 208 blobs/files.
- Relevant areas include governance, verification, security, backend tests, frontend tests, architecture documentation, and KCN security/verification modules.

Representative files:
- `ARCHITECTURE.md`
- `governance/README.md`
- `verification/README.md`
- `backend/app/routes/governance.py`
- `backend/app/routes/verification.py`
- `backend/tests/test_governance.py`
- `backend/tests/test_security_fabric_foundation.py`
- `security/README.md`
- `verification/*`

File presence establishes artifact existence only; it does not establish runtime execution or qualification.

### Quantara Core

At `3e981a860b954329f8a4fc4f44a5b7f0c09ff2c1`:
- Root includes architectural/legal/research documentation, a `src/` TypeScript implementation, tests, and historical/webarchive artifacts.
- Representative files:
  - `ARCHITECTURAL_BLUEPRINT.md`
  - `CREATOR_POLICY.md`
  - `QUANTARA_MASTER_DNA.md (The "Full Solve" Annex).txt`
  - `Quantara_Core_Mathematical_Annex.md`
  - `src/index.ts`
  - `src/config.ts`
  - `src/services/apiService.ts`
  - `tests/unit/qed_engine.test.ts`
  - `tests/integration/api.test.ts`
  - `tests/security/rls.test.ts`

### Quantara Physics Labs

At `4b2d7bfc0f4f4d68af1a957aa28cd6f2cd94a98d`:
- Current `main` state is a merge commit with two parents.
- Commit message begins `Lovable update`.
- Tree identity: `d2fc9224c94531a4c278393a6cb2022e97aa51b6`.
- The tree contains application source, Supabase migrations, and test suites.
- This state is an artifact identity anchor only.

## 8. Relationship classifications established in this pass

### R001 — Historical/current state relationship
KSI Benchmark Suite:
`aef8a1ea...` → `f710816c...`
Relationship: predecessor → successor; current adds `Procfile`.

### R002 — Historical/current state relationship
MANIFEX:
`e7660b8f...` → `00a41ce1...`
Relationship: predecessor → successor; current is 13 commits later and adds Experiment-001 / ER-v2 implementation/evidence material.

### R003 — Canonical evolution
Canonical:
`01c0d11b...` → EA-G1 commit series → `b7723bf5...`
Relationship: state evolution.
Exact terminal EA-G1 anchor remains OPEN.

### R004 — KCN branch identity
`copilot/kcn-super-cognitive-ecosystem` is the repository default branch and currently resolves to `cf8ca49...`.
Relationship: current/default branch → identified commit.

### R005 — Quantara current-state identity
Quantara Physics Labs and Quantara Core are now cryptographically anchored to current default-branch commits.
Relationship between the two repositories themselves remains unresolved; same creator/name family is not treated as proof of derivation or equivalence.

## 9. Findings

### F001-IDENTITY-DRIFT — ESTABLISHED

Existing provenance records and current repository heads may legitimately refer to different states of the same repository.

Therefore repository identity must be represented as a time/state graph rather than a single mutable repository record.

This is established as a reconciliation requirement.

Not established:
- that the current state is superior;
- that the historical state is inferior;
- that either state is verified;
- that either state is qualified.

### F002-CANONICAL-STATE-PROLIFERATION — ESTABLISHED

The canonical repository is not one immutable system state.

At minimum it contains:
- historical baseline `01c0d11b...`;
- EA-G1 implementation series;
- current EA-G2 state `b7723bf5...`.

Therefore all future evaluation records must bind results to an exact commit/tree/artifact identity.

### F003-IMPORT-MANIFEST-PRESERVATION — ESTABLISHED

The existing import manifest correctly preserves historical source commits even when source repositories later advance.

Its historical source references must not be rewritten merely to match current heads.

### F004-STATE-CONTINUITY — ESTABLISHED FOR KSI BENCHMARK

The KSI Benchmark Suite current head is exactly one commit ahead of the imported state, with the imported commit as merge base and `Procfile` as the only changed file.

This is a direct Git relationship, not an inference.

### F005-MANIFEX-STATE-EVOLUTION — ESTABLISHED

The MANIFEX current head is 13 commits ahead of the imported `e7660b8f...` state.

The current state materially expands the repository with execution-evidence/registration implementation, tests, and Experiment-001 / ER-v2 documentation.

Therefore the imported Build Index artifact and current MANIFEX repository must be tracked as different state nodes.

### F006-KCN-MERGE-STATE — ESTABLISHED

The identified KCN state `cf8ca49...` is a merge commit with two parents.

It must not be modeled as a simple linear continuation without retaining its two-parent topology.

### F007-EA-G1-ANCHOR-OPEN — OPEN

EA-G1 exists as a series of commits, but one exact terminal commit representing the complete EA-G1 state has not yet been established.

### F008-TAG-RELEASE-ENUMERATION-OPEN — OPEN

A complete tag/release inventory was not established in this connector pass.

No tag/release is being inferred from branch names, commit messages, or repository labels.

## 10. Unresolved identity work

The following remain OPEN:

1. Exact terminal EA-G1 commit.
2. Exhaustive branch inventory for every repository.
3. Complete tag/release inventory.
4. Exact historical/current tree comparison for every repository in the recovery baseline.
5. Exact duplicate/copy detection across repositories at blob level.
6. Exact predecessor/successor/fork/derivative relationships for KCN-II, KCN-AGSI-ASI, KSI, Global Intelligence, and Quantara repositories.
7. Resolution of the specific KSI-ASI-001 source artifact relationship; repository location alone is insufficient.
8. Runtime/execution identity for each implementation.
9. Evaluation-result identity bound to exact executable state.
10. Independent verification identity.
11. Qualification state.
12. Human ratification state.

## 11. Explicit non-findings

This registry does NOT establish:

- correctness of historical benchmark scores;
- execution of every identified repository;
- integration between repositories;
- qualification of any system;
- independent verification;
- production readiness;
- authority delegation;
- patent filing or patent-pending status;
- scientific validity of Quantara claims;
- superiority of current heads over historical states.

## 12. Next forensic operation

Pass 001 continues with:

1. Exhaustive relevant branch/tag/release resolution.
2. Exact artifact-level duplicate detection.
3. Cross-repository blob identity comparison.
4. Import-copy verification against source-state blobs.
5. Predecessor/successor/fork/derivative graph construction.
6. Identity conflict registry population.
7. Only after identity reconciliation: transition to FORENSIC-001-CLAIM-REGISTRY.

**Bottom line:** the repository/state distinction is now demonstrated by direct Git evidence, not merely a modeling preference. The KSI Benchmark and MANIFEX examples provide concrete predecessor/successor chains, while the canonical repository demonstrates multi-stage evolution through baseline → EA-G1 series → EA-G2/current.


## 13. Artifact-level reconciliation pass

This sub-pass compared the seven existing `legacy/` blobs in the forensic branch against the identified source-state trees.

### Exact source-blob matches

The following legacy artifacts have exact Git blob identity with the corresponding historical/current source state:

| Legacy artifact | Source repository/state | Source path | Blob SHA | Relationship |
|---|---|---|---|---|
| `legacy/MANIFEX/manifex/build_index.py` | MANIFEX @ `e7660b8f...` | `manifex/build_index.py` | `ad0256cf...` | EXACT COPY |
| `legacy/KSI-Benchmark-Suite/benchmark/grader.py` | KSI Benchmark @ `aef8a1ea...` | `benchmark/grader.py` | `72efce9c...` | EXACT COPY |
| `legacy/KSI-Benchmark-Suite/mlops/replacement_policy.py` | KSI Benchmark @ `aef8a1ea...` | `mlops/replacement_policy.py` | `4c339b07...` | EXACT COPY |
| `legacy/KSI-Benchmark-Suite/mlops/run_student_benchmark.py` | KSI Benchmark @ `aef8a1ea...` | `mlops/run_student_benchmark.py` | `d575188d...` | EXACT COPY |

The same four source blobs are also present in the canonical repository's legacy paths, confirming preservation of those exact source artifacts.

### Source-snapshot wrappers

The following are **not exact blob copies** of their source README files:

- `legacy/KCN/README.source.md`
  - legacy blob: `f7eabeb2...`
  - source KCN `README.md` blob at `cf8ca49...`: `285091cd...`
- `legacy/KSI/README.source.md`
  - legacy blob: `086ddafa...`
  - source KSI `README.md` blob at `91360e7...`: `1220525a...`

Direct content inspection shows both legacy files are provenance wrappers containing source metadata and then the source README content. They therefore represent **preserved source snapshots/wrappers**, not byte-identical copies of the original README blobs.

The KCN wrapper explicitly records source repository, source branch, and source blob SHA `285091cd...`. The KSI wrapper explicitly records source repository, source branch, and source blob SHA `1220525a...`.

### Negative result

No exact blob match was found, among the identified twelve current/default source-state trees, for the following legacy wrapper blobs beyond their expected presence in the canonical repository itself:

- KCN `README.source.md`
- KSI `README.source.md`
- canonical `legacy/README.md`

This is a negative identity result only. It does not establish that the underlying source content is absent elsewhere.

## 14. New artifact-reconciliation findings

### F009 — EXACT-COPY-PROVENANCE — ESTABLISHED

Four preserved legacy artifacts are cryptographically identical to files at their recorded historical source states:

- MANIFEX `build_index.py`
- KSI Benchmark `grader.py`
- KSI Benchmark `replacement_policy.py`
- KSI Benchmark `run_student_benchmark.py`

This establishes exact artifact identity and source-state correspondence. It does **not** establish execution, correctness, verification, or qualification.

### F010 — PROVENANCE-WRAPPER-DISTINCTION — ESTABLISHED

KCN and KSI `README.source.md` artifacts are wrappers containing source metadata plus preserved README content. Their wrapper blob SHA is necessarily different from the source README blob SHA.

Therefore file-name/content similarity alone must not be used as an exact-copy test.

### F011 — CROSS-REPOSITORY-BLOB-CHECK — ESTABLISHED

The exact-blob comparison across the twelve identified current/default source-state trees confirms that the four source-code legacy artifacts above map to their expected source repositories/states.

No unexpected cross-repository exact-blob relationship was established in this limited seven-legacy-artifact corpus.

## 15. Reconciliation boundary

This artifact pass establishes **exact-copy relationships**, not complete provenance.

Still required:

1. Compare every relevant canonical `legacy/` artifact against all historical source states, not only the current/default states.
2. Resolve whether any source files were renamed or transformed while retaining equivalent content.
3. Expand blob comparison to every preserved import/archive artifact.
4. Compare historical source-state trees against canonical imported trees.
5. Construct explicit copy/import edges with source commit, source tree, source blob, destination path, and destination blob.
6. Detect forks/derivatives using tree overlap and commit ancestry rather than names.
7. Resolve the remaining repositories and historical commits in the recovery baseline.

The identity graph therefore now contains both **state-level edges** and the first **artifact-level exact-copy edges**.


## 16. Pass 004 lineage-tracing findings

### R006 — KCN SOURCE-REFERENCE EDGE — ESTABLISHED

The canonical capability registry contains explicit source-artifact references to four artifacts in the historical KCN Phase-1 architecture state:

- KCN `intelligence/README.md`
  - source commit: `cb1ddde4b94cce3868f620a5d6c12d958ed28fc1`
  - source blob: `0bb6d5b8922c18a453e523d057e34e6337565d21`
- KCN `backend/tests/test_intelligence.py`
  - source blob: `0413f0e5184d4ba3c6892df54289af671eb385d1`
- KCN `verification/README.md`
  - source blob: `cbe78628a80c00c38f2153aae0c9122331849fcf`
- KCN `ARCHITECTURE.md`
  - source blob: `9bb6f67d5baabb8c0b46cd59c5b75bbd81394620`

Those blob identities were independently recovered from the KCN historical tree at `cb1ddde4...`, whose commit message is `feat: complete Phase 1 foundation architecture scaffold`.

The canonical registry entries were introduced on 2026-10-02 in canonical commits:

- `235ab94aa21d2430e9bf23bc9da2a528e19f73c2` — register source-traceable capabilities
- `80b5d0b5762d744846b240c634b5a5e1f75f3148` — expand source-traceable capability inventory

This establishes a direct, cryptographically anchored **source-reference relationship** from canonical capability-registry records to exact historical KCN artifacts.

Classification of the canonical registry relationship to those KCN artifacts:

**REFERENCE_ONLY — ESTABLISHED**

This does not establish that the registry is a copied or adapted implementation of those KCN files. It establishes that the canonical artifact intentionally records those exact KCN artifacts as evidence-bearing source references.

### F015 — KCN HISTORICAL SOURCE-STATE RECOVERY — ESTABLISHED

The relevant KCN architecture did not originate at the previously anchored September merge state.

The earliest recovered commit containing `ARCHITECTURE.md` and the governance/intelligence/verification foundation is:

`cb1ddde4b94cce3868f620a5d6c12d958ed28fc1`

dated 2026-08-01.

Its tree contains 153 blobs.

Exact blob comparison against the canonical tree at the 2026-10-02 System-of-Systems architecture state found zero byte-identical blobs. However, the canonical capability registry independently records exact SHA-256 source identities for KCN artifacts from this historical state.

Therefore:

- exact source-reference lineage: ESTABLISHED;
- exact code/file-copy lineage from KCN historical tree into canonical current tree: NOT ESTABLISHED;
- adapted-copy lineage: NOT ESTABLISHED;
- derivative lineage: NOT ESTABLISHED.

### F016 — HISTORICAL-ANCHOR-WAS-INSUFFICIENT — ESTABLISHED

The KCN source commit originally used as the forensic repository anchor (`cf8ca49...`) is not sufficient by itself to represent the earliest relevant source state.

The historical architecture commit `cb1ddde4...` predates the September merge state and contains the exact KCN artifacts later referenced by canonical capability-registry evidence.

This validates the Pass-003 hypothesis that a manifest source commit can be a provenance anchor without necessarily being the historical artifact-origin point.

### R007 — KSI HISTORICAL ENUMERATION — PARTIAL / UNRESOLVED

KSI README history shows an initial commit on 2026-06-22 followed by successive README updates and replacement-content commits before the anchored `91360e7...` state.

No exact canonical blob match or explicit source-reference edge to the anchored KSI repository was established in this pass.

The KSI → canonical relationship remains **UNRESOLVED**.

### R008 — MANIFEX ENGINEERING OS HISTORICAL ENUMERATION — PARTIAL / UNRESOLVED

The capability-registry/architecture state is anchored at:

`c7a19803b732fc8fe8abf29a8f46daec869585a5`

with parent `b5274a3896d42cc2e31fe7ffd2906e7ba1762f61`.

The commit explicitly adds `MANIFEST/CORE-CAPABILITY-REGISTRY.md`.

The source registry contains concepts overlapping the canonical capability/evidence/provenance architecture, including E0–E5, provenance ledger, evidence ledger, and capability inventory.

No exact canonical blob match or independent source-reference edge to this MANIFEX Engineering OS artifact was established.

Classification remains **UNRESOLVED**.

### R009 — MANIFEX ENGINEERING → EVIDENCE — UNRESOLVED

The examined source state `2b1e0ec...` is a one-file initial README commit.

No exact canonical blob match or independent historical commit/reference edge was established.

Classification remains **UNRESOLVED**.

### R010 — KCN-AGSI/ASI — UNRESOLVED

No exact canonical blob match or independently supported historical lineage edge for the specific `KSI-ASI-001` source artifact was established.

The absence of a located source artifact is not treated as proof that none exists.

Classification remains **UNRESOLVED**.
