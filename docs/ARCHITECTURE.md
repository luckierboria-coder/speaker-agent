# Architecture — Acoustic Target Drives the Pipeline

## Core position
SpeakerAgent is a model-neutral engineering tool layer. It never includes an AI model, and it does not reimplement COMSOL/ANSYS/FEMM as a general solver. External Codex/Claude/etc. agents and a local UI consume the same constrained deterministic tools.

## Data flow
1. Acoustic goal and its measurement environment
2. Feasibility and scope/assumption checks
3. Low-cost small-signal electromechanical + radiation model
4. Feasible-region / Pareto fitting of target system parameters
5. Structural fitting and acoustic FEM/BEM cross-check
6. Motor fitting to requested BL/Le with FEMM or other approved tools
7. Recompute end-to-end acoustic response and compare to the original goal
8. Test / calibration / report / approved revision

This is an iterative bidirectional coupling. Magnetics is a constraint-fitting submodule, not the primary optimizer.

## Software topology
- Python 3.12+ package for validation, automation, orchestrated job state, numerical analysis and connector contracts.
- Internal engineering quantities use SI; external I/O declares units, axes and acoustic dB references.
- Solver adapters are capability-described and swappable: analytic/0D electromechanical; 2D/3D pressure acoustics; structural FEM; magnetic FEMM, etc.
- Avoid requiring a particular paid solver for initial M0 contract tests.
- A CLI is the first control plane, with optional MCP and local GUI later; no bundled LLM.

## Crucial acoustic requirements
- Every SPL value has reference pressure 20 µPa in air, RMS convention and field/drive/measurement conditions; absolute pressure at unspecified reference is rejected.
- Record excitation (input voltage RMS, supplied current or power), electrical loading, temperature/medium, distance, direction, and baffle/fixture geometry.
- Distinguish full electroacoustic forward response from imposed-velocity acoustic radiation: prescribing velocity ignores source feedback unless coupling explicitly exists.
- Linear piston models have restricted frequency and displacement validity and cannot accurately promise high-frequency breakup or harmonic distortion.
- Keep simulation target tolerances and acceptance criteria as separate signed records.

## Provenance / controls
Store all input data, source/revision, topology, solver settings/version, mesh checks, model limits, result status and comparison metrics. No fabricated results. Protect expensive or destructive runs behind engineer approval.

## First installed solver priority
A validated small-signal electroacoustic reference model / supported acoustics workflow; FEMM reserved for motor fitting later. Engineers' existing tools take precedence.
