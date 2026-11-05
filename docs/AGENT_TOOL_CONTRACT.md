# External-Agent Tool Contract — Acoustic First (draft)

SpeakerAgent is a deterministic tool layer callable from Codex, Claude, other external agents or an engineer GUI. No bundled AI.

## Proposed namespaced tools (not implemented yet unless stated)
- acoustic_target.validate, acoustic_target.describe
- measurement.import, measurement.validate
- solver.list, solver.capabilities, solver.health
- acoustic.forward_model, acoustic.compare_reference
- acoustic.infer_feasible_parameters, acoustic.rank_candidates
- driver.mechanical_fit, motor.fit_to_required_parameters
- simulation.prepare, simulation.run, simulation.status, simulation.results
- design.close_loop, design.compare
- report.export

## Contracts
Inputs always include project/revision, topology, frequency sampling, SPL reference definition, drive/measurement conditions, baffle and acoustic load, constraints and solver preferences. Responses include units, algorithm/model version, input hash, observables, verification status, numerical diagnostics, declared assumptions, feasibility, convergence and provenance.

## Error taxonomy
MISSING_MEASUREMENT_CONDITION, INVALID_REFERENCE, OUT_OF_MODEL_RANGE, UNIDENTIFIABLE_INVERSE_PROBLEM, NO_FEASIBLE_SOLUTION, MISSING_MATERIAL, SOLVER_NOT_INSTALLED, LICENSE_UNAVAILABLE, MESH_FAILURE, NONCONVERGED, TIMEOUT, CANCELLED, INVALID_INPUT.

## Guardrails
- Never invent measured or computed frequency response or reference material data.
- Never equate 2.83 V with 1 W except at 8 ohm nominal resistive load under explicitly suitable conditions.
- If model conditions differ from target conditions, return an incompatibility diagnostic instead of a score.
- An external LLM may plan calls; actual physics is computed only by explicitly installed and validated tools.
- Human approval for destructive edits, costly runs and manufacturing release.

## Stage priority
Acoustic target, model and validation first. Motor-fitting tools are introduced only after electromechanical targets are derived and validated.
