# Acoustic Benchmark and Validation Plan — M0/M1

## Benchmarks to acquire (no result currently validated)
A. Analytic electromechanical circuit checks: units, DC limit, resonant frequency consistency, passivity, expected motion/impedance shape.
B. Idealized baffled rigid piston radiation: compare suitable analytic expressions in explicitly defined far-field and validity range; include complex phase where supported.
C. Published COMSOL lumped speaker (Application ID 12295): inspect licensing/availability and record original model source, version, parameters, solver setup and output curves before comparing.
D. A real driver: measured impedance and frequency response at matched excitation, baffle, distance, air temperature and axis; requires actual product/fixture data.

## Acceptance ladder
V0 — input schema and metadata tests in CI, no solver.
V1 — independent analytic checks for the forward model.
V2 — external solver comparison, identical boundary/load/drive conditions.
V3 — measured driver correlation, including uncertainty and measurement setup.

## Acceptance metrics — to be frozen before reference run
- Relative and absolute error metrics with frequency windows defined separately for impedance and pressure.
- Frequency sampling, interpolation/smoothing, phase convention and normalization set in advance.
- Mesh refinement for field solvers at >=3 resolutions, with monitored observables and documented criteria.
- Repeated runs must report solver version, OS, hash, run conditions and deviations.
- Failed, incomplete, ill-conditioned or physically inapplicable cases are NOT accepted as valid.

## Existing numerical values
NONE. All physical response targets/metrics and computed values await an independently sourced model or engineer-supplied measurement.

## References
https://www.comsol.com/model/lumped-loudspeaker-driver-12295
https://www.comsol.com/support/learning-center/course/modeling-speaker-drivers-in-comsol-multiphysics-202/modeling-speaker-drivers-lumped-methods-88401
