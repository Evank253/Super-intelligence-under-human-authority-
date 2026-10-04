# KCN-AKIIS Capability Benchmark — Evolution Policy

## Purpose

This policy permits future benchmark generations to evolve while preserving CB-v1.0 as immutable historical evidence.

## Version boundary

- **CB-v1.0** remains the frozen historical baseline.
- Future generations use new version identifiers such as **CB-v2.0**, **CB-v3.0**, etc.
- A future generation must live in its own versioned directory and/or branch.
- No future generation may modify files under `capability-benchmark-v1/`.

## What may evolve

Future generations may introduce:
- new unseen tasks;
- harder adversarial tasks;
- new transfer tasks;
- domain expansion;
- improved evaluator criteria;
- improved reference material;
- new scoring dimensions;
- refreshed human/expert baselines;
- improved execution harnesses.

Every change must receive a new corpus hash and benchmark manifest.

## What must remain comparable

When a generation is intended to be compared with v1, the report must separately identify:

1. **Historical baseline:** results obtained on the exact CB-v1.0 corpus.
2. **Evolution result:** results obtained on the new generation corpus.
3. **Delta:** any measured change attributable to the new generation, without treating different task sets as directly equivalent measurements.

A new task set must never be described as a rerun of v1.

## Required evidence chain for every generation

**Versioned corpus → freeze → actual system invocation → preserved raw outputs → independent scoring → domain results → capability vector → human interpretation**

No system-generated score, historical scorecard, or self-certification may substitute for independent evaluation.

## Required records

Each generation should contain, at minimum:

- benchmark protocol;
- scoring rubric;
- exclusion rules;
- model-facing task corpus;
- evaluator-only references;
- task manifest;
- freeze manifest;
- execution records;
- raw-output records;
- independent evaluation records;
- final capability vector.

## Regression rule

CB-v1.0 remains the fixed regression baseline. If a future system generation is evaluated for longitudinal comparison, rerun the exact frozen v1 corpus separately from the new evolution corpus.

**Historical corpus status:** immutable  
**Future evolution status:** permitted  
**Capability claim:** remains NOT ESTABLISHED until independently measured for the relevant execution.
