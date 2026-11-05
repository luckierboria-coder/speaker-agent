# SpeakerAgent

**Agent-ready engineering tools for acoustic-target-driven loudspeaker driver design.**

SpeakerAgent is a deterministic, AI-provider-neutral engineering tool layer. It connects acoustics, electromechanical modeling, structural geometry and motor fitting through existing CAD/CAE/measurement software used by acoustic engineers. It does **not** bundle a language model, implement a new FEM solver, or demand a migration from an established COMSOL/ANSYS/MATLAB/KLIPPEL workflow. External Codex/Claude or other agents may use its validated tools.

## Design principle: acoustic goal first

Acoustic performance target (FR/SPL/directivity and test conditions)
→ physics/feasibility checks
→ small-signal electroacoustic forward model and parameter fitting
→ diaphragm/suspension geometry fitting
→ motor fitting to required BL/Le/Re and stroke
→ acoustic re-simulation, verification, design revision.

A target is not a result. A fitted equivalent model is not proof of an actual manufacturable driver. A single response curve does not uniquely determine motor geometry.

## Current status: M0 engineering preparation

**Implemented in repository:** planning specs; basic typed engineering contracts; acoustic target conditions and sampled SPL target validation; synthetic-contract unit tests; benchmark registry; CI configuration.

**Not implemented/verified:** physical acoustic predictions, COMSOL or other acoustic solver integration, completed physical acoustic benchmark, FEMM execution, driver-measured calibration, mechanical and motor design fitting, external-agent tool transport or GUI.

## Roadmap

| Stage | Deliverable |
| --- | --- |
| M0 | Acoustic target/measurement specification, data model, validation requirements and adapter capability interfaces |
| M1 | Small-signal acoustic forward prediction, benchmark validation and feasible electromechanical parameter search |
| M2 | Diaphragm/suspension structural fitting and acoustic-structure cross-checks |
| M3 | Motor design fitting for required BL/Le/thermal limits, with full acoustic loop re-evaluation |
| M4+ | Nonlinear distortion, thermal behavior, production tolerance analysis and more driver types |

See [roadmap](docs/ROADMAP.md) and [project overview](docs/PROJECT_OVERVIEW.md).

## Documentation

- [Acoustic-target-first engineering spec](docs/M0_M1_ENGINEERING_SPEC.md)
- [Acoustic target input requirements](docs/engineering/ACOUSTIC_TARGET_REQUIREMENTS.md)
- [Benchmark validation plan](docs/engineering/ACOUSTIC_BENCHMARK_PLAN.md)
- [Material data policy](docs/engineering/MATERIAL_DATA_POLICY.md)
- [CAD and geometry interface](docs/engineering/CAD_AND_GEOMETRY_INTERFACE.md)
- [Solver capabilities](docs/engineering/SOLVER_CAPABILITIES.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Agent tool contract](docs/AGENT_TOOL_CONTRACT.md)
- [Development setup](docs/DEVELOPMENT.md)

## Install M0 contract tests (Windows PowerShell)

Requires Python 3.12+:

```powershell
git clone https://github.com/luckierboria-coder/speaker-agent.git
cd speaker-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
```

These are only metadata and contract tests; they do not run a physics solver or verify a speaker prediction.

## Evidence status and licensing

The official COMSOL [Lumped Loudspeaker Driver reference model](https://www.comsol.com/model/lumped-loudspeaker-driver-12295) is an intended independent benchmark, not a result that has already been reproduced. No production sample, measured curve or certified materials have yet been received.

No license has been selected for this repository. The repository may be public, but its contents are not automatically open-source licensed. Do not commit confidential customer drawings, measurements, or material curves.
