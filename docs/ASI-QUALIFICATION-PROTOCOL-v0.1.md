# ASI Qualification Protocol v0.1

Status: PROPOSED / NOT EXECUTED

## Objective
Determine whether a frozen integrated KCN + MANIFEX + KSI implementation
demonstrates broad, repeatable, independently verifiable problem-solving
performance sufficient to support a system-level superintelligence claim.

## Evidence rule
Architecture -> Implementation -> Verification -> Qualification -> Human Ratification.
No stage may be skipped. Historical results are not silently substituted for
current integrated-system evidence.

## Evaluation dimensions
1. Generality across materially different domains.
2. Novel transfer on previously unseen task structures.
3. Multi-step reasoning and error correction.
4. Long-horizon execution.
5. Engineering: create, debug, test, repair.
6. Scientific/technical problem solving with expert adjudication.
7. Tool selection and use.
8. Robustness under adversarial and degraded conditions.
9. Evidence discipline and calibration.
10. Governance and inability to self-authorize.
11. Reproducibility.
12. Comparative performance against strong human, AI, and human+AI baselines.

## Task policy
Final holdout tasks must be hidden, frozen before execution, stratified by
domain/difficulty, resistant to contamination, and independently adjudicated
when exact ground truth is unavailable. The holdout cannot be tuned after
results are observed.

## Comparator policy
Comparators must be preregistered before final execution and use consistent
task definitions, resource budgets, and scoring rules. Include strong
individual human, human-team where appropriate, relevant frontier AI,
specialized solver/tool, and human+AI baselines.

## Statistics
Report sample sizes, domain scores, confidence intervals, effect sizes,
failure rates, missing-data handling, multiple-comparison handling, and
sensitivity analysis. No aggregate score may conceal catastrophic domain
failures.

## Authority attack tests
Attempt to induce the system to promote its own evidence state, bypass
qualification, grant itself authority, treat confidence as truth, treat
execution success as authorization, or alter/delete provenance. Record every
failure.

## Threshold
No numeric ASI threshold is asserted in v0.1. A threshold must be
preregistered after the task distribution, comparator, resource budget, and
statistical power are defined.

## Outcome states
NOT MEASURED; OBSERVED; VERIFIED; QUALIFICATION CANDIDATE; QUALIFIED;
NOT QUALIFIED.

QUALIFIED may only be assigned after independent review and human
ratification, and qualification never confers authority.

## First executable milestone
EA-G2: Integrated Evaluation Harness Smoke + Invariant Campaign.

EA-G2 must execute a frozen task packet, record task/submission/result data,
hash evidence records, preserve NOT_MEASURED, prevent authority escalation,
and produce a reproducible report.
