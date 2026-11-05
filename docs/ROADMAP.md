# SpeakerAgent Roadmap — Acoustic-Target-First

Status: revised architecture and proposed milestones; no physics validation has yet occurred.

## M0.1 — Acoustic target engineering contract (NOW)
- Define acoustic performance targets with reference conditions: frequency, dB SPL, tolerance bands, distance, axis angle, baffle, driving quantity (V_rms or power), acoustic medium, measurement window and provenance.
- Define system constraints: outer diameter, mounting geometry, usable stroke, budget, power/thermal limits and manufacturable part families.
- Establish units and schema, explicit missing-data states, machine-readable tests, benchmark provenance and model capability declarations.
- Exit: target definitions round-trip reproducibly, and invalid/ambiguous conditions are rejected.

## M0.2 — Acoustic reference and interfaces (NOW)
- Create nonfabricated benchmark registry: trusted analytic rigid-piston and small-signal equivalent-circuit calculations, and cited third-party validated reference models (e.g., COMSOL Lumped Loudspeaker Driver).
- Define solver adapters and standardized inputs/outputs for acoustics, mechanical, electromagnetic and measurements without tying the core to one vendor.
- A dry-run adapter and CI tests test contracts only, not physical accuracy.
- Exit: reference case and acceptance protocol agreed; external solver is not mandatory to test contracts.

## M1.1 — Small-signal forward acoustic model
- Implement or connect deterministic equivalent electro-mechanical circuit and acoustic radiation model for a specified boundary condition.
- Predict impedance, cone velocity/displacement, on-axis SPL where source assumptions permit, and relevant acoustic-load quantities.
- Validate first against analytical cases, then independently against a trusted model or measurement.
- Exit: full test conditions, applicable frequency/linearity regime, numerical residual and known limitations reported.

## M1.2 — Target fitting / feasible-region search
- Fit families of Mms, Cms, Rms, BL, Re and Le (subject to topology and material constraints) to a measured/declared acoustic target, with ambiguity and tradeoffs explicit.
- Return ranked feasible sets/Pareto candidates, sensitivity and failure reasons; do not equate fitted abstract parameters with manufacturable designs.
- Exit: candidates reproducibly improve a stated acoustic objective without violating hard constraints.

## M1.3 — Acoustic higher-fidelity integration
- Prefer an engineer's existing COMSOL or other proven acoustic/structural solver. Support 2D axisymmetric or 3D FEM/BEM as geometry requires.
- Model radiation baffle, near/far field, cavities and diaphragm deformation as justified by frequencies.
- Exit: at least one independently reviewed coupled acoustic reference case with documented convergence and cross-checks.

## M2 — Physical mechanics
- Fit cone/diaphragm/suspension geometry and materials to the electromechanical target region.
- Structural modal and dynamic verification; push updated model properties back into acoustic simulation.

## M3 — Motor fitting (NOT the first-stage priority)
- Fit magnet, gap, coil and steel geometry to demanded BL(x), Le(x,i), resistance, heat and stroke constraints, using FEMM/COMSOL or the engineer's tools.
- Mechanical and motor parameter updates must close the acoustic-performance verification loop.

## M4+ — Nonlinearity, thermal, production and topology extensions
- Harmonic/intermodulation distortion, temperature and compression, uncertainty, tolerance analysis, BOM, production testing, microspeakers/tweeters/other topologies.

## Do not conflate
- An acoustic target is not an achieved response.
- An equivalent-circuit fit is not a verified physical structure.
- A solver API smoke test is not a magnetic/acoustic validation.
- Frequency response at one condition is not sufficient to uniquely determine BL or motor geometry.

## Official model references
- https://www.comsol.com/model/lumped-loudspeaker-driver-12295
- https://www.comsol.com/support/learning-center/course/modeling-speaker-drivers-in-comsol-multiphysics-202/modeling-speaker-drivers-lumped-methods-88401
