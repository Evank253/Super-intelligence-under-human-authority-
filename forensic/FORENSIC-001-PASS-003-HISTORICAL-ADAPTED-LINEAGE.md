# FORENSIC-001 — PASS 003: HISTORICAL / ADAPTED LINEAGE RECONCILIATION

**Date:** 2026-10-05  
**Forensic branch:** `forensic-001/recovery-manifest`  
**Prior tree-reconciliation baseline:** `b3b06a95d5b294051375da5530b00cb87362d839`  
**Canonical state examined:** `Evank253/Super-intelligence-under-human-authority-@` `b7723bf5b31f97b56eb45235f66e3bf6badb184a`

## Objective

Attack unresolved lineage rather than perform another broad inventory.

The target relationship is:

`SOURCE REPOSITORY → SOURCE STATE → SOURCE ARTIFACT → CANONICAL ARTIFACT → EVIDENCE → RELATIONSHIP CLASS`

The pass explicitly distinguishes evidence of provenance from evidence of implementation correctness, execution, verification, qualification, or authority.

## Invariants

1. Similarity is not derivation.
2. Naming is not lineage.
3. A provenance statement is a claim unless independently supported.
4. A zero exact-blob result is not proof of no lineage.
5. Historical source states remain distinct.
6. A later source state cannot silently replace an earlier candidate import state.
7. Adaptation requires evidence of identifiable source lineage plus modification.
8. Transformation requires demonstrable lineage despite substantial representational change.
9. UNRESOLVED remains distinct from NO_RELATIONSHIP_ESTABLISHED.
10. No lineage finding promotes qualification or authority.

## Historical-state observations

### KCN

The previously anchored state is:

- repository: `Evank253/KCN-SUPER-COGNITIVE-HUMAN-GOVERNED-INTELLIGENCE-ECOSYSTEM-`
- commit: `cf8ca49b872a9baaa7212caba28837f486d54062`
- tree: `8577031ff35985231c56ec8e46887db2163e34cc`
- source-tree size examined: 208 blobs.

The commit is a merge commit with parents:

- `20090fb834e9271ebf84b40d68b2b932ff120bb4`
- `e0aadacb557372d25a5dd2d255b19bc3df637047e`

This establishes that the named KCN source state itself has nontrivial historical ancestry and should not be treated as the only possible source state.

The KCN repository contains explicit human-governance architecture, including documentation describing human governance as the top-level authority and human review/approval for high-risk operations. It also contains governance, intelligence, verification, security, and evidence-oriented components.

**However:** those conceptual overlaps do not establish that the canonical repository's corresponding architecture was derived from KCN.

**Current classification against canonical system:** UNRESOLVED.

### KSI

Previously anchored source state:

- repository: `Evank253/Ketchums-Super-Intelligence-KSI-`
- commit: `91360e7e146f8b870098c30f0fed38ea484ba3a3`
- tree: `88e86f62ed7f445a6ed9c79ed0b6f55781be08e4`
- source-tree size examined: 66 blobs.

The repository history includes an earlier upload sequence for the KSI application, including individual files for swarm agents, safety components, tools, and web application components. Therefore the current anchored state should not be assumed to be the original implementation state.

No exact canonical blob was established from the anchored state.

Searches for explicit `KSI-ASI`, `authority`, and `human authority` provenance terms in the KSI source repository did not return indexed matches.

**Current classification against canonical system:** UNRESOLVED.

### MANIFEX Engineering OS

Anchored source state:

- repository: `Evank253/MANIFEX-ENGINEERING-OS`
- commit: `c7a19803b732fc8fe8abf29a8f46daec869585a5`
- tree: `4e67107cb925bac067039569de79d5ec1bc1f54d`
- source-tree size examined: 7 blobs.

The source history identifies `c7a19803...` as a documentation commit adding the MANIFEX core capability registry and architecture map. Earlier history includes capability/integration inventory and authorship/rights records.

No exact canonical blob was established from this source state.

The canonical import manifest records the source artifact as an intended `ADAPT` action. That is an intended relationship/action, not independent proof that a descendant artifact exists.

**Current classification:** UNRESOLVED.

### MANIFEX Engineering → Evidence

Anchored source state:

- repository: `Evank253/MANIFEX-ENGINEERING-TO-EVIDENCE`
- commit: `2b1e0ec5e365a9b4dae8978221796edb95729623`
- source state is the repository's initial commit.
- source tree examined: 1 blob.

No exact canonical blob was established.

Because this source state is a single initial README artifact, semantic lineage cannot responsibly be promoted from conceptual overlap alone.

**Current classification:** UNRESOLVED.

### KCN-AGSI/ASI

Anchored source repository:

- `Evank253/KCN-AGSI-ASI`
- examined state: `16c3da0d9f131f55685095f5bfd1bcf8b27c18b2`

No exact canonical blob was established.

The prior recovery finding remains: a specific `KSI-ASI-001` artifact was not located in the current search.

**Current classification:** UNRESOLVED.

### KCN-II

Anchored source state:

- `Evank253/KCN-II @ 5c63cdf57e464813f514794b5e67bcc030b2f225`
- 121 source blobs examined.

No exact canonical blob was established.

**Current classification:** UNRESOLVED.

### Global Intelligence

Anchored source state:

- `Evank253/Global-Intelligence @ 754fb1ff22da0de58ec4db525f137d09a06ae75a`
- 790 source blobs examined.

No exact canonical blob was established.

**Current classification:** UNRESOLVED.

## Important distinction: source architecture vs canonical architecture

The KCN source contains explicit human-governance concepts that overlap strongly with the mission represented by the canonical repository.

That is useful evidence of **conceptual correspondence**.

It is not sufficient evidence of:

- copied implementation;
- adapted implementation;
- transformed implementation;
- derivative implementation;
- shared commit ancestry;
- source-code descent.

Accordingly, no KCN → canonical ADAPTED_COPY or DERIVATIVE edge is established by this pass.

The same boundary applies to KSI and MANIFEX.

## Historical-state risk discovered

The current source-state anchors are not necessarily the actual import points.

For example:

`KSI repository → early upload state → later KSI state → current anchored state`

and:

`KCN repository → parent A / parent B → merge state`

mean that comparing only the current named state can miss the actual artifact that was historically copied or adapted.

Therefore, a future exact-lineage search must enumerate candidate historical states before assigning a final negative lineage result.

## Preliminary classification matrix

| Source | Current anchored state | Exact blob result | Adapted/derived evidence | Classification |
|---|---|---:|---|---|
| KCN | `cf8ca49...` | 0 | conceptual overlap only | UNRESOLVED |
| KSI | `91360e7...` | 0 | no sufficient lineage evidence | UNRESOLVED |
| MANIFEX Engineering OS | `c7a19803...` | 0 | manifest says ADAPT; artifact proof absent | UNRESOLVED |
| MANIFEX Engineering → Evidence | `2b1e0ec...` | 0 | conceptual role only | UNRESOLVED |
| KCN-AGSI/ASI | `16c3da0...` | 0 | specific KSI-ASI-001 not located | UNRESOLVED |
| KCN-II | `5c63cdf...` | 0 | none established | UNRESOLVED |
| Global Intelligence | `754fb1f...` | 0 | none established | UNRESOLVED |

## What is actually established

At the end of Pass 003, the strongest established ancestry remains:

- MANIFEX `e7660b8...` → `manifex/build_index.py` → canonical `legacy/MANIFEX/manifex/build_index.py` = EXACT_COPY.
- KSI Benchmark `aef8a1a...` → three benchmark artifacts → corresponding canonical `legacy/KSI-Benchmark-Suite/` artifacts = EXACT_COPY.
- KCN and KSI README wrappers = WRAPPED_COPY / provenance wrappers.

Everything beyond those demonstrated edges remains either unresolved or a negative exact-blob result.

## Next operation

The next pass should become **historical commit-to-artifact lineage tracing**.

Priority:

1. enumerate KCN's relevant parent/earlier states;
2. enumerate KSI's initial upload and pre-anchor states;
3. enumerate MANIFEX Engineering OS history around capability-registry creation;
4. inspect canonical commit history for introduction of candidate architecture artifacts;
5. compare candidate source trees against canonical trees at the relevant historical points;
6. use path-history and commit diffs to identify rename/adaptation events;
7. only then evaluate transformed/derivative relationships.

No relationship will be promoted solely because two repositories describe similar architecture.

## Status

**Pass 003 status: PARTIAL / LINEAGE STILL UNRESOLVED**

This pass successfully narrowed the question and exposed the principal remaining uncertainty: the manifest's named source commits may be provenance anchors, but they are not necessarily the historical commits from which every canonical artifact originated.

That uncertainty is now explicitly recorded rather than silently resolved.

# PASS 004 ADDENDUM — HISTORICAL COMMIT-TO-ARTIFACT TRACING

## KSI implementation-origin recovery

The previously examined KSI commit 45190320c2bc45362bbfdd9dfb1bac717814347a is the repository's README-only initial commit. It is therefore not the origin of the later KSI implementation.

The KSI implementation was uploaded as a linear sequence beginning on 2026-06-22. Earliest recovered implementation commits include:

- 15e15aa30c726a3f9ac3b4590af475e995d45d99 — README update
- a48d041e603799853d13120777f72a59fd0fa400 — runtime.txt
- 4b1fdd77d113d3684c3ad5c869d4c24e3293c933 — docker-compose.yml
- 338def3a8b2cd5891bca2e0210d92f74df8d0cec — emergent integration
- f99fd023ea7843bff61ecede0aa7c2847673c41c — capability matrix
- 46669e9631facf87c5bf567aa441ce244c6ffdcc — key-rotation specification
- faa9ae3e5fc5e540f2c2f6bd1d000d655800286c — root-control initialization
- fc8e6ab17dcb6e6af27e9ccb003a068eabbf237c — constitution engine
- 4031fc171f2c80380ccbd72c809fee84748a11aa — kernel router
- 41e8bfe54da166ff45bd49ca1bcea5aa9ae5dddc — safety alignment engine
- 146444cbd2cc9dd996f91925e761146011aa381a — architecture documentation

The later anchored KSI head 91360e7e146f8b870098c30f0fed38ea484ba3a3 is only the terminal point of this initial upload history.

No exact blob match from the KSI source tree to the canonical Python-3 tree was established, and repository-wide indexed searches did not establish an explicit canonical-source reference to the KSI repository. KSI implementation lineage therefore remains UNRESOLVED.

Similar names such as constitution, root control, safety, router, and capability matrix are not sufficient to classify canonical KSI-ASI architecture as copied, adapted, transformed, or derivative.

## Canonical architecture introduction boundary

The canonical repository contains explicit authority/evidence separation artifacts, including specifications/KSI-ASI-001.md, architecture/authority-boundaries.md, architecture/capability-evidence-authority.md, and architecture/capability_registry.yaml.

KSI-ASI-001 currently states VERIFICATION: NOT YET ESTABLISHED and defines forbidden promotion paths including confidence→evidence, confidence→authority, successful execution→authority, and qualification→human authorization.

The canonical capability registry independently records exact KCN source artifact identities for KCN capabilities. This establishes explicit KCN REFERENCE_ONLY lineage, but does not establish KSI implementation descent.

## Pass 004 classification boundary

| Candidate lineage | Classification | Basis |
|---|---|---|
| KCN historical artifacts → canonical capability registry | REFERENCE_ONLY | Exact source repository/path/blob identities independently match the historical KCN tree and are explicitly recorded in the canonical registry |
| KSI historical implementation → canonical implementation | UNRESOLVED | Historical implementation origin recovered, but no exact blob or independent source-reference edge established |
| MANIFEX Engineering OS → canonical | UNRESOLVED | Historical capability-registry state recovered, but no exact blob or independent source-reference edge established |
| MANIFEX Engineering → Evidence → canonical | UNRESOLVED | No sufficient artifact/history evidence established |
| KCN-AGSI/ASI → KSI-ASI-001 | UNRESOLVED | Specific source artifact still not independently located |

## New forensic conclusion

Pass 004 demonstrates that historical source-state enumeration changes the evidentiary picture. It does not automatically produce lineage. It identifies the states at which lineage can now be tested.

The next high-value operation is artifact-to-artifact comparison at the canonical introduction commit, especially for authority/evidence architecture and canonical files that explicitly reference historical source artifacts.

UNRESOLVED remains the correct classification wherever that comparison cannot establish a supported lineage edge.