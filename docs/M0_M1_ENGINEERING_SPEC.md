# M0/M1 Engineering Specification

## Reference scope
Conventional axisymmetric moving-coil magnetic motor; 2D r-z cross section. This is a reference implementation, not the only planned driver architecture.

## Canonical coordinates
r: radial position in meters, r >= 0.
z: axial position in meters.
x: axial voice-coil displacement relative to the documented nominal rest position, meters. Define +x explicitly in each reference fixture.
All stored quantities use SI units; UI may show millimeters, tesla, newtons per ampere, ohms.

## Inputs
Topology ID and template version; part geometry (magnet, yoke, pole, top plate, gap, coil); coil turns, active conductor directions and winding distribution; material identifiers and B-H curve revision; relevant air domain; boundary conditions; excitation; mesh controls; x sweep; geometric tolerance and cost assumptions.

## Outputs
Magnetic field B(r,z), gap flux density sampling definition, magnetic energy when supported, BL(x) in newtons per ampere, useful-stroke flatness metric, mass/volume estimates, solver logs, warnings, and validation records.

## Physics and numerical definitions
BL(x) must have a documented derivation from current-driven Lorentz force or the solver's verified force/flux-linkage method, with force sign conventions and current normalization explicit. Handle coil movement consistently; no interpolation or assumed constant gap field may be presented as a high-fidelity BL(x) result.

An optional normalized flatness objective over stroke [-X, +X]:
E = (1/(2X)) * integral(((BL(x) - BL(0))/BL(0))^2 dx).
Reject when BL(0) is zero or invalid. This is one selectable design metric, not a universal industry standard.

## Early constraints
- Positive thickness/height; physically possible stack-up and radial clearance.
- Material assignments and B-H data present and versioned.
- Magnetic saturation evaluated against reference material behavior.
- Coil excursion and clearance checked across requested sweep.
- Compare winding, current and displacement conventions across all runs.

## Verification strategy
1. Unit tests: schema, dimension conversion, invalid overlaps, material completeness.
2. Physics fixtures: independently inspected motor geometry and field/BL curves.
3. Mesh refinement: tolerance on specified observables, not just mesh element count.
4. Repeatability: same solver/settings/input reproduce outputs within fixed numerical tolerance.
5. Comparison: FEMM output vs reference FEM or trusted measurements; document disagreement conditions.
6. Regression: saved fixture revisions and approved result tolerances.

## Explicit limitations
FEMM axisymmetric magnetostatics does not itself provide full 3D acoustic response, diaphragm breakup, nonlinear THD, or thermal compression. Never infer these from a magnetic field plot alone.
