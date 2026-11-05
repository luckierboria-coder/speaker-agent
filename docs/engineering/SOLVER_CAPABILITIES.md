# Acoustic-first Solver Adapter Capabilities (M0 contract)

Adapter metadata includes solver name/version, installed state, license need, operating system, model form (0D circuit, 2D axisymmetric FEM, 3D FEM/BEM, measured-data import, mechanical FEM, magnetic FEM), supported frequency range/condition assumptions, and accepted geometry/material representations.

Every adapter must:
- reject unsupported physics and inconsistent target measurement conditions;
- record input revision, source file hash, units, load/baffle, drive and output reference conventions;
- capture solver version, command/log, mesh/convergence and artifact hashes;
- return structured status: unavailable, validation failed, running, completed unverified, verified against a reference, or failed;
- distinguish acoustic radiation from coupled electroacoustic voltage-driven prediction.

First adapter priority: small-signal electro-mechanical forward reference with a compatible acoustic radiation model. COMSOL lumped loudspeaker model is a reference / prospective interface, not a currently installed dependency.

Later physical-domain adapters: structural FEM for diaphragm/suspension; FEMM/COMSOL magnetic motor design constrained by required BL and Le.

The core should remain runnable and unit-testable without any commercial solver or built-in AI model.
