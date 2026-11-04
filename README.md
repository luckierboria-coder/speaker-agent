# SpeakerAgent

**Agent-ready, model-agnostic engineering tools for loudspeaker driver design.**

SpeakerAgent is an engineering tool layer for practical loudspeaker-driver development. It is designed for acoustic engineers who want to use their existing CAD, CAE, simulation, and measurement software with external agents such as Codex or Claude.

> **Important:** SpeakerAgent does not embed or bundle a language model and does not attempt to replace existing commercial solvers.

## Goals

- Standardize loudspeaker design parameters, units, constraints, material provenance, simulation tasks and results.
- Expose validated engineering operations through a Python core, then CLI/MCP adapters for external agents.
- Prioritize interoperability with the software already used by engineers (FEMM first, COMSOL and other tool adapters later).
- Run reproducible physical simulations and optimization tasks with explicit convergence/verification checks.
- Support conventional cone drivers first while retaining an extensible framework for miniature, tweeter and other transducer architectures.
- Keep engineers in control of input assumptions, expensive jobs and release decisions.

## Current stage: M0 foundation (not yet a working solver)

The repository contains initial engineering specifications, a Python project skeleton, minimal solver-neutral data contracts, unit tests, and CI configuration.

**Implemented:** core project structure, a basic SI scalar/input contract, smoke tests, and documentation.

**Not yet implemented:** FEMM solver adapter, motor parameterized geometry, BL(x) extraction, solver validation, optimization, GUI, MCP integration, or COMSOL connectivity.

## Roadmap overview

| Milestone | Goal |
| --- | --- |
| M0 | Engineering data model, input validation, tool contract and diagnostics |
| M1 | Verified 2D axisymmetric moving-coil magnetic motor workflow with FEMM and optimization |
| M2 | Lumped electroacoustic models and measurement comparisons |
| M3 | Diaphragm and suspension structural models |
| M4 | 3D acoustic and multiphysics solver adapters |
| M5+ | Nonlinear and thermal modeling, tolerances, BOM and production workflows |

See [the full roadmap](docs/ROADMAP.md).

## Documentation

- [Project scope and boundaries](docs/PROJECT_OVERVIEW.md)
- [Software architecture](docs/ARCHITECTURE.md)
- [Engineering specification for M0/M1](docs/M0_M1_ENGINEERING_SPEC.md)
- [Agent tool contract (draft)](docs/AGENT_TOOL_CONTRACT.md)
- [Development setup](docs/DEVELOPMENT.md)

## Quick start (M0 only)

Requires Python 3.12+.

```powershell
git clone https://github.com/luckierboria-coder/speaker-agent.git
cd speaker-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
```

The command above exercises data-contract tests only; it does **not** run a loudspeaker simulation. FEMM/COMSOL remain separate installations subject to their licenses.

## Engineering principles

1. Prefer existing engineer software and workflows over a replacement platform.
2. Keep language models external, optional and swappable.
3. Separate agent recommendations from verified numerical computation.
4. Report units, solver versions, input provenance, mesh checks and limitations.
5. Do not claim physical validity until validated against trusted references or measurements.

## Licensing

No open-source license has been selected yet. Until one is added, standard copyright rules apply. Do not assume this public repository grants broad reuse rights.
