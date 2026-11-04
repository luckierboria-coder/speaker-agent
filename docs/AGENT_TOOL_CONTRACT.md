# External-Agent Tool Contract (draft)

The project is agent-ready, but AI-provider-neutral. Calls to engineering tools are explicit JSON-compatible operations, not generated unrestricted code.

## Proposed tools
- project.create / project.load / project.snapshot
- topology.list / topology.describe
- material.list / material.inspect
- design.validate
- geometry.preview
- solver.list / solver.capabilities / solver.health
- simulation.prepare / simulation.run / simulation.status / simulation.results
- design.evaluate / design.compare
- optimization.propose / optimization.run / optimization.status
- report.export

Names and payloads remain provisional until M0.1 schemas and automated tests are adopted.

## Standard request concepts
project_id, revision_id, topology_id, model_version, variable map with unit-typed values, solver preference, allowed run budget, approval token for protected actions.

## Standard response concepts
run_id, status (queued/running/succeeded/failed/cancelled), engine/version, input snapshot hash, artifact references, diagnostics, result units, verification status, limitations.

## Error taxonomy
INVALID_INPUT, MISSING_MATERIAL, UNSUPPORTED_PHYSICS, SOLVER_NOT_INSTALLED, LICENSE_UNAVAILABLE, MESH_FAILURE, NONCONVERGED, TIMEOUT, CANCELLED, ARTIFACT_CORRUPT.

## Human-in-the-loop controls
External agents can create proposals and request verified engineering actions. A user must approve high-cost batches, deletion or replacement of artifacts, and release of designs into manufacturing. Solver output must not be silently fabricated, backfilled or converted into a measured claim.

## Future transports
Prefer a deterministic Python/CLI core; add MCP tools for Codex/Claude and a desktop GUI without duplicating physics logic.
