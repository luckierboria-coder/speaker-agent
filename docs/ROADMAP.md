# Development Roadmap

Status: planning. No solver integration or validation is claimed yet.

## M0.1 — Foundational contracts
Deliverables: repository skeleton; units policy; topology and material schemas; tool catalogue; error/status taxonomy; reproducibility metadata; fixture and tests.
Exit: reference project can be validated, serialized and reloaded without losing units or provenance.

## M0.2 — Deterministic tool runtime
Deliverables: local CLI callable from external agents; clean tool boundaries; structured logs; dry-run mode; input and file validation.
Exit: stable contract tests for errors and successful dry runs; no model dependency.

## M1.1 — Axisymmetric motor geometry
Deliverables: initial conventional ferrite/neodymium motor template; voice coil and gap coordinate conventions; checks for overlaps and manufacturability.
Exit: representative reference geometries produce consistent 2D cross sections.

## M1.2 — FEMM adapter and BL(x)
Deliverables: FEMM installation diagnostics; material B-H curves; axisymmetric magnetostatic model creation; meshing; sweep of coil position; force-factor calculation; field data and reports.
Exit: repeatable run with documented mesh sensitivity and cross-check against an independently verified reference.

## M1.3 — Parametric optimization
Deliverables: constrained sweeps; multiple design objectives; candidate comparison and Pareto frontier; restartable run history.
Exit: automatic optimization improves a defined objective without violating hard constraints.

## M1.4 — External-agent skill / tool integration
Deliverables: minimal MCP or CLI adapter, example prompts, safe tool actions, human confirmation boundaries, concise run summaries.
Exit: at least two external clients can execute the same workflow without a bundled LLM.

## M2 — Lumped electroacoustic models
T/S parameter calculations; impedance/low-frequency predictions; measured-data imports; comparison/uncertainty.

## M3 — Structural design
Cone, surround and spider geometry adapters; structural FEA; modal and stiffness validation.

## M4 — 3D acoustic and multiphysics
Commercial solver adapters; radiation, near/far field and directivity; coupling, mesh convergence and measurement correlation.

## M5+ — Nonlinear, thermal and production integration
BL(x), Kms(x), Le(x,i), thermal compression, tolerancing, BOM, cost and engineering approval workflows.

## Work policy
Do not add a new physics area before the preceding reference calculations are validated. Prefer one reliable automated engineering operation to many impressive but unverifiable features.
