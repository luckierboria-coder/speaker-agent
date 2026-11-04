# Architecture

## Primary design
A headless, deterministic engineering tool core exposes a documented interface. External agents (Codex, Claude, others) can call those tools; an optional GUI makes them directly usable by engineers. The tool core has no embedded AI.

Logical layers:
1. Engineer UI / external agent client.
2. Tool API and policy checks (input validation, permissions, run budgets).
3. Project model: topology, geometry, material provenance, parameters, units, boundary conditions, objectives, revision.
4. Domain workflows: motor, diaphragm, suspension, acoustic radiation, thermal (independent stages).
5. Solver adapters: FEMM first; COMSOL / ANSYS / MATLAB / existing vendor systems as permissions and interfaces allow.
6. Postprocessing, uncertainty, verification, comparison and export.
7. Artifact storage and run audit trail.

## Technology decisions (initial)
- Python 3.12+ for orchestration and engineering data processing.
- Standard Python package; no GUI required to operate the core.
- JSON-schema-compatible typed inputs and outputs; SI units internally.
- NumPy / SciPy for numeric processing when introduced.
- FEMM for baseline 2D axisymmetric magnetostatic calculations where the installed environment supports it.
- UI, workflow server, database and optimizer chosen only when concrete requirements justify their complexity.
- Support future MCP and/or CLI tool exposure without coupling the core to a specific AI provider.

## Solver adapter contract
Every adapter must identify the solver and version, check installation and license availability, declare supported physics and dimensions, prepare a deterministic input, run synchronously or return a job handle, capture logs and convergence status, export normalized results, and report structured failures. Never label a failed or unconverged run as successful.

## Data provenance
Persist project revision, topology template version, input geometry and material identifiers, material B-H curves, excitation/conditions, mesh controls, solver version, run status, outputs, validation checks, and timestamps. Hash or content-address input snapshots to permit exact comparisons.

## Safety / reliability boundaries
- No arbitrary source execution from untrusted prompts.
- Validate units, ranges, intersecting components, missing material properties, and unsupported topologies before solver execution.
- Separate an agent's proposed action from the engine's verified and executed action.
- Expose human confirmation gates for destructive operations, costly jobs and design release.
- Explicitly distinguish simulated, measured, inferred and estimated results.

## Future extensibility
Create new transducer templates and physics adapters without rewriting common project formats. 3D acoustic and structural analysis use the same orchestration records but different required inputs and validation rules.
