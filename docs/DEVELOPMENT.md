# Development Guide — M0 Acoustic First

Requires Python 3.12+, Git. No FEMM or COMSOL installation is required for M0 metadata tests.

## Setup
```powershell
git clone https://github.com/luckierboria-coder/speaker-agent.git
cd speaker-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ruff check .
```

## Current modules
- src/speaker_agent/core/contracts.py: generic finite-valued engineering input with units.
- src/speaker_agent/core/acoustic_targets.py: acoustic targets, voltage/power excitation, SPL reference and test-condition validation.
- docs/engineering: measurement requirements, CAD, materials, solver contract and benchmark plan.
- benchmarks/acoustic: reference registry. No validated frequency response or SPL exists yet.
- benchmarks/production-driver: pending manufacturer-provided sample and measurements.
- src/speaker_agent/solvers/femm: reserved later motor-fitting adapter namespace; no functionality.

## Engineering workflow
1. Acoustic target and experimental fixture conditions.
2. Forward small-signal electroacoustic model, compared with independent analytical/reference cases.
3. Inverse parameter fitting yielding feasible regions; quantify ambiguity.
4. Diaphragm/suspension physical fit.
5. Motor BL/Le/Re fitting and return to acoustic re-simulation.

## Next ticket
Acquire and verify an independently reproducible acoustic reference, then implement a simple small-signal forward prediction with input/condition metadata and actual numerical regression tests.

## Governance
- No embedded AI model.
- Existing engineering apps preferred.
- Never declare physically verified based on schema/CI-only tests.
- No company drawings/test records/material datasets committed to a public repository unless authorized.
