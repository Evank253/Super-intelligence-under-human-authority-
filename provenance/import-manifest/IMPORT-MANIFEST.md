# Import Manifest

This manifest is the controlled inventory of recoverable prior work.

| Source repository | Source ref/commit | Source artifact | Original status | Proposed destination | Action | Verification |
|---|---|---|---|---|---|---|
| Evank253/MANIFEX | e7660b8f6342f2de0c407a6dc1ea66a782b0b3fe | manifex/build_index.py | Implemented artifact in source repo; independent verification pending | evidence/provenance + verification | ADAPT | NOT MEASURED |
| Evank253/KSI-Benchmark-Suite | aef8a1ea28739a9d01a332993990e8e370aa3bb6 | mlops/run_student_benchmark.py | Implemented benchmark runner | benchmarking/runner | ADAPT | NOT MEASURED |
| Evank253/KSI-Benchmark-Suite | aef8a1ea28739a9d01a332993990e8e370aa3bb6 | benchmark/grader.py | Implemented fallback grader | benchmarking/evaluators | ADAPT | NOT MEASURED |
| Evank253/KSI-Benchmark-Suite | aef8a1ea28739a9d01a332993990e8e370aa3bb6 | mlops/replacement_policy.py | Implemented policy helper | benchmarking/evaluators | FREEZE / REVIEW | NOT MEASURED |
| Evank253/MANIFEX-ENGINEERING-TO-EVIDENCE | 2b1e0ec5e365a9b4dae8978221796edb95729623 | README.md | Clone-based engineering-to-evidence architecture | evidence / provenance | ADAPT | NOT MEASURED |
| Evank253/MANIFEX-ENGINEERING-OS | c7a19803b732fc8fe8abf29a8f46daec869585a5 | architecture/capability registry documentation | Architecture capture | architecture / capability registry | ADAPT | NOT MEASURED |
| Evank253/KCN-SUPER-COGNITIVE-HUMAN-GOVERNED-INTELLIGENCE-ECOSYSTEM- | cf8ca49b872a9baaa7212caba28837f486d54062 | governance/intelligence/verification/security architecture | Large prior KCN implementation | legacy/KCN | FREEZE / AUDIT | NOT MEASURED |
| Evank253/Ketchums-Super-Intelligence-KSI- | 91360e7e146f8b870098c30f0fed38ea484ba3a3 | repository architecture and application | Prior KSI implementation | legacy/KSI | FREEZE / AUDIT | NOT MEASURED |
| Evank253/KCN-AGSI-ASI | repository located; specific KSI-ASI-001 artifact not found by current search | prior ASI work | Prior experiment | legacy/KSI | AUDIT | OPEN |

## Rules

1. Source repositories remain unchanged.
2. Imports preserve source commit/ref and path.
3. Copying an artifact does not promote its evidence status.
4. Historical metrics remain historical until underlying artifacts are recovered and independently verified.
5. Missing artifacts remain OPEN / EVIDENCE REQUIRED.
6. The manifest itself is an audit artifact, not a certification.

## Source hashes recovered during audit

- MANIFEX `manifex/build_index.py` blob SHA: `ad0256cf9b95ae61b82d6a2e6312dfd7ab438461`
- KSI benchmark runner blob SHA: `d575188d8690d7010de0785663d38748ebaa9f3c`
- KSI fallback grader blob SHA: `72efce9c056f829c73a8aeeb15e079716d504e30`
- KSI replacement policy blob SHA: `4c339b07d102729a5cba10c8c4452498ff877d5a`
- MANIFEX-ENGINEERING-TO-EVIDENCE README blob SHA: `e67da408fc4d8ae39107505227c005b57d7e5f8d`
- MANIFEX-ENGINEERING-OS README blob SHA: `c94d160b8cb0eede4e23a58e8f55396e59c4972d`

These hashes identify the retrieved source blobs; they do not certify the claims contained within them.


## Tree-level reconciliation pass — 2026-10-05

### Scope

Compared the complete blob inventories of the canonical Python-3 head (`b7723bf5...`) against the identified source-state trees for the first reconciliation set. This is an artifact-identity comparison, not a semantic derivation proof.

### Results

| Source state | Source blobs | Exact blob matches in canonical head | Determination |
|---|---:|---:|---|
| MANIFEX @ `e7660b8f...` | 2 | 1 | Partial exact import established |
| MANIFEX Engineering OS @ `c7a19803...` | 7 | 0 | No exact blob import established |
| MANIFEX Engineering → Evidence @ `2b1e0ec5...` | 1 | 0 | No exact blob import established |
| KSI Benchmark Suite @ `aef8a1ea...` | 17 | 3 | Partial exact import established |
| KCN @ `cf8ca49...` | 208 | 0 | No exact blob import established |
| KSI @ `91360e7...` | 66 | 0 | No exact blob import established |
| KCN-AGSI/ASI @ `16c3da0...` | 1 | 0 | No exact blob import established |
| KCN-II @ `5c63cdf...` | 121 | 0 | No exact blob import established |
| Global Intelligence @ `754fb1f...` | 790 | 0 | No exact blob import established |

### Confirmed exact import edges

1. MANIFEX `manifex/build_index.py` → `legacy/MANIFEX/manifex/build_index.py`
   - blob: `ad0256cf...`

2. KSI Benchmark `benchmark/grader.py` → `legacy/KSI-Benchmark-Suite/benchmark/grader.py`
   - blob: `72efce9c...`

3. KSI Benchmark `mlops/replacement_policy.py` → `legacy/KSI-Benchmark-Suite/mlops/replacement_policy.py`
   - blob: `4c339b07...`

4. KSI Benchmark `mlops/run_student_benchmark.py` → `legacy/KSI-Benchmark-Suite/mlops/run_student_benchmark.py`
   - blob: `d575188d...`

### Important interpretation

The canonical import manifest labels several source artifacts as `ADAPT`, even where the preserved legacy artifact is an exact blob copy. These are not contradictory:

- **artifact identity:** exact copy;
- **intended destination/action:** ADAPT;
- **verification:** NOT MEASURED.

The registry must preserve all three dimensions.

For MANIFEX-ENGINEERING-OS and MANIFEX-ENGINEERING-TO-EVIDENCE, zero exact blob matches means only that no byte-identical source blob was found in the canonical current head. The manifest's `ADAPT` action may still have produced transformed/adapted descendants; semantic lineage remains unresolved.

For KCN, KSI, KCN-AGSI/ASI, KCN-II, and Global Intelligence, zero exact blob matches likewise does **not** prove absence of lineage. It establishes only a negative result for exact Git blob identity against these particular source states.

### New forensic findings

**F012 — PARTIAL-TREE-IMPORT — ESTABLISHED**

The canonical repository contains exact source-state artifacts from MANIFEX and KSI Benchmark Suite, but not complete source trees.

**F013 — ZERO-BLOB-RESULT-IS-NOT-NO-LINEAGE — ESTABLISHED**

A zero exact-blob match is a negative result for byte identity only. It cannot by itself distinguish ADAPTED, TRANSFORMED, REFERENCE_ONLY, DERIVATIVE, or NO_RELATIONSHIP_ESTABLISHED.

**F014 — ACTION/IDENTITY SEPARATION — ESTABLISHED**

The import manifest's intended action (`ADAPT`, `FREEZE / REVIEW`, etc.) is a separate provenance dimension from the artifact's actual cryptographic identity.

### Remaining tree-reconciliation work

1. Compare every historical import commit, not only the currently identified source state.
2. Resolve renamed files using Git history and path changes.
3. Compare transformed artifacts using structural/semantic evidence.
4. Identify canonical documentation that explicitly references source repositories or artifacts.
5. Reconcile the canonical `legacy/` directory against all historical import states.
6. Establish derivative/fork relationships only where evidence supports them.
7. Keep `UNRESOLVED` distinct from `NO_RELATIONSHIP_ESTABLISHED`.
