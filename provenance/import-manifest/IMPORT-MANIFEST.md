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
