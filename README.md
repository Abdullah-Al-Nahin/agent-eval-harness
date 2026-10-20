# Agent-Eval-Harness: Automated Code Synthesis & Verification Benchmark

A modular, lightweight evaluation testbed designed to benchmark language model agents on multi-lingual code synthesis, automated error recovery, and static verification.

## Key Features
- **Sandboxed Subprocess Execution:** Isolated test runners with strict timeout controls.
- **Standardized Metrics:** Automatic calculation of Pass@1, syntax error frequency, runtime exception rates, and execution latency.
- **Extensible Task Sets:** JSON-driven test definitions with integrated unit testing baselines.

## Quickstart
    git clone https://github.com/Abdullah-Al-Nahin/agent-eval-harness.git
    cd agent-eval-harness
    python examples/evaluate_dummy.py --tasks benchmarks/tasks.json --output results/run_01.json

## Research & Academic Citation
Developed as part of an undergraduate research initiative into autonomous agent orchestration at **American International University-Bangladesh (AIUB)**.

## License
MIT License - Copyright (c) 2026 Abdullah Al Nahin
