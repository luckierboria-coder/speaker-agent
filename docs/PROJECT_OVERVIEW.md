# SpeakerAgent — Project Overview

## Mission
Build an engineer-ready, model-agnostic tool layer for loudspeaker driver development. Engineers should be able to use existing CAD/CAE/measurement applications through Codex, Claude, or another external agent, without learning to program.

## Product boundaries
- SpeakerAgent does NOT bundle, host, or require a language model.
- SpeakerAgent is NOT a replacement for COMSOL, ANSYS, MATLAB, KLIPPEL, LOUDSOFT, or CAD.
- SpeakerAgent is NOT a new finite-element or acoustic solver.
- It provides validated engineering tools, normalized data contracts, solver adapters, repeatable workflows, and traceable results.
- Existing commercial engineering workflows take priority; avoid forced migration.
- Human engineers approve requirements, geometry changes, expensive runs, and release decisions.

## First product family
General loudspeaker-driver design is the long-term goal: cone drivers, tweeters, miniature drivers, and later specialized transducers. Physics and geometry modules are topology-specific; the orchestration core stays common.

## First milestone
M0: canonical data contracts, units, versioned project records, tool interface, diagnostic records, tests.
M1: a verified 2D axisymmetric moving-coil motor workflow using FEMM, including field maps, BL(x), constraints, optimization, and reports.
A COMSOL adapter is a later expansion, not a prerequisite to the first working demonstration.

## Definition of usable
An acoustic engineer selects an approved template, enters dimensions and engineering constraints, launches a tool-driven simulation, sees convergence and objective metrics, compares versions, and can export a reproducible result. A connected external agent can perform the same workflow through a stable tool interface.

## Explicitly out of scope for M0/M1
Full 3D acoustic radiation, diaphragm breakup, suspension nonlinearity, THD prediction, mass-production drawings, manufacturing sign-off, and model-generated unvalidated simulation code.
