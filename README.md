# Agent-Eval-Harness: Automated Code Synthesis & Verification Benchmark

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23515338.svg)](https://doi.org/10.5281/zenodo.23515338)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

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
Developed as part of an undergraduate research initiative into autonomous agent orchestration at **American International University-Bangladesh (AIUB)**. Published via Zenodo under DOI [10.5281/zenodo.23515338](https://doi.org/10.5281/zenodo.23515338).

## License
MIT License - Copyright (c) 2026 Abdullah Al Nahin
