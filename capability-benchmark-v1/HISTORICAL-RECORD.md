# KCN-AKIIS Capability Benchmark v1.0 — Historical Evidence Record

**Status:** HISTORICAL / FROZEN  
**Benchmark:** CB-v1.0  
**Corpus:** 140 tasks across 7 domains  
**Freeze state:** BENCHMARK-FROZEN  
**Execution at freeze:** NOT STARTED  
**Scoring at freeze:** NOT STARTED  
**Capability:** NOT MEASURED  
**Capability claim:** NOT ESTABLISHED

## Immutable evidence anchor

The canonical frozen corpus is preserved at the following Git commit:

- Repository: `Evank253/Super-intelligence-under-human-authority-`
- Freeze branch: `capability-benchmark-v1-freeze`
- Freeze commit: `073a12243ffc872b0bcc5a7b568dfb0060cb9db1`
- Task corpus SHA-256: `154ccc0c09ea1daace67a8737d05598273c279b1b011cbce1b2d548f4e450930`
- Freeze manifest SHA-256: `2be2ae24fd3d9d79b922d8a69507b200b46202427b6515db5f04f7269f712903`

The v1 task text, scoring rubric, exclusion rules, evaluator references, manifests, and bound hashes are historical evidence and must not be edited in place.

## Historical-use rule

CB-v1.0 may be executed in the future as a **frozen regression benchmark**, but its task corpus must remain byte-for-byte unchanged. Any later execution is a new execution record against the same historical corpus; it does not modify the benchmark definition.

## Evolution boundary

Future benchmark generations must use a new version identifier and separate generation directory/branch. They may add, replace, or refine tasks and evaluation criteria, but those changes must never overwrite CB-v1.0.

**Required distinction:** historical comparability is preserved by rerunning the exact frozen v1 corpus; capability evolution is measured by separately versioned future corpora.

## Prohibited mutation

Do not edit or replace the CB-v1.0 task files, rubric, exclusion rules, evaluator references, task manifest, or freeze manifest as part of future benchmark development.

