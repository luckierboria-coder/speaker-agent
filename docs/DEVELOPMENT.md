# Development guide

## Requirements
Python 3.12+, Git. FEMM is an external Windows application and is NOT required for the M0 tests.

## Setup
1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the package with: python -m pip install -e ".[dev]"
4. Execute: python -m pytest -q
5. Optionally run: python -m ruff check .

## Repository structure
- docs/: project decisions, architecture, roadmap, specifications, tool contract.
- src/speaker_agent/core/: shared validated data contracts.
- src/speaker_agent/solvers/: external solver adapter namespaces.
- src/speaker_agent/agent_interface/: provider-neutral external agent integration.
- tests/: deterministic contract and later physics validation tests.
- examples/: future reproducible reference fixtures.

## Integration rules
- Keep the physics execution separate from the language-model client.
- Preserve units and solver input provenance in every result.
- No unreviewed changes to real engineering models or licenses.
- Prefer integrations with existing engineer tools over replacing those tools.
- Mark an unverified physical result as unverified.

## First development ticket
Define machine-readable JSON-compatible schemas for topology, geometry, material provenance, run configuration, result status and engineering quantities. Freeze a first baseline fixture before implementing the FEMM adapter.
