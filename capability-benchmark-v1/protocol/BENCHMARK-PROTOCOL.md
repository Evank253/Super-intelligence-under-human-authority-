# Capability Benchmark v1.0 Protocol

Purpose: measure empirical task capability without using the existing KCN-AKIIS scorecard.

Design: 140 frozen unseen tasks across science, engineering, mathematics, strategy, creativity, planning, and research. Each domain contains 10 core, 5 adversarial, and 5 transfer tasks.

For every execution preserve the exact task, exact raw output, implementation commit, runtime metadata, timestamp, exit status, stdout/stderr when applicable, and SHA-256 hashes.

The evaluator scores the preserved raw output against evaluator-only criteria. KCN-generated scores, confidence, certification labels, and performance reports are not scoring inputs.

Aggregate first to a seven-dimensional capability vector. A single aggregate score, if later used, must have an explicit independent methodology.

Any execution deviation from the frozen corpus creates a separate measurement record.
