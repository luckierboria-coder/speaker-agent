# SpeakerAgent — Project Overview

## Mission
Build an engineer-ready, model-neutral tool layer for loudspeaker driver development. It helps engineers achieve specified ACOUSTIC targets first, then derive electromechanical targets and fit physical driver designs using existing CAE/CAD/measurement tools. Codex, Claude, or another external agent may control these tools; the package contains no AI model.

## Product boundaries
- Not a new multiphysics solver and not a replacement for COMSOL, ANSYS, MATLAB, KLIPPEL, LOUDSOFT or an engineer's CAD.
- No hosted, bundled or compulsory LLM; external AI integration remains optional.
- Reuse commercial engineering tools and measured data whenever available; deliver a well-defined CLI and later MCP tool layer.
- Separate the target, idealized acoustic predictions, electromechanical feasible-region search, physical geometry fitting, high-fidelity verification and measured validation.
- Engineers approve assumptions, constraints, expensive runs and manufacturing release.

## Guiding workflow — acoustic first
1. Declare measurable acoustic requirements and test conditions.
2. Build a lightweight acoustic/electromechanical approximation to assess feasibility.
3. Inverse-fit feasible families of mass/compliance/loss/force-factor/impedance parameters. Do not claim a unique inverse solution.
4. Fit diaphragm, surround, spider, coil and magnetic geometry to those feasible families.
5. Re-run acoustics using high-fidelity or measured-derived parameters, evaluate and iterate.
6. Record deviations, uncertainties, fabrication constraints and provenance.

## Scope and prioritization
General loudspeaker drivers (cone drivers, tweeters, microspeakers, later specialized types). Common orchestration, topology-specific physics models.

M0: acoustic target and measurement-condition data contracts, units, versioning, reference cases, solver capability contracts and verification standards.
M1: end-to-end acoustic-first *small-signal* reference workflow, using an equivalent electromechanical model coupled to an appropriate acoustic radiation model; compare to independent analytical and/or official solver references.
M2: diaphragm, suspension and acoustic-structure refinement with external FEM/BEM where available.
M3: motor fitting (FEMM/COMSOL/other approved tools) to demanded BL/Le/current/thermal constraints; close the acoustic loop.
M4+: nonlinear, thermal and specialized driver topologies.

## Current status
Specifications and minimal Python contracts only. No acoustic or magnetic finite-element solver has been executed or physically validated through this repository. No production drawing or measurement data has been supplied.
