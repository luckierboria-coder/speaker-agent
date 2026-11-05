# CAD / Geometry Interchange — Acoustic First

Status: specification only; import/export not implemented.

## Scope
Existing CAD workflows and source drawing revisions remain authoritative. The first geometric interfaces describe the radiating diaphragm, dustcap, surround, mechanical frame/baffle opening, acoustic cavities and boundary geometry. Magnet geometry is deferred.

## Parametric representation
- Right-handed local r-z coordinates for axisymmetric conventional drivers: r from axis, z toward designated acoustic front. Full 3D drivers use XYZ, with a declared transform.
- Store effective radiating area Sd and the geometry or measurement from which it was derived; do not assume nominal outer diameter is Sd.
- Distinguish piston approximation (effective area and assumed velocity) from actual cone shape, mode shapes and structural mesh.
- Store front/rear radiation regions, baffle size and test fixture IDs. These determine output and cannot be omitted in comparisons.
- Define interfaces to import dimensional drawing and DXF profiles (AutoCAD 2022 compatible), and later STEP/IGES where the installed CAD allows.

## Interchange checks
- Record drawing provenance, units, coordinate mapping, scale and source hash.
- Use declared DXF entities and part/layer mapping. Reject open/self-intersecting profiles, unsupported 3D entities and silent mirrored geometry.
- Validate gap between acoustic moving components and the frame for expected displacement before claiming physical fit.
- Comparison previews must show the imported source and generated geometry overlay, subject to engineer approval.

## Outputs
A normalized geometric configuration, validation report, traceable imported drawing references and later geometry input for the engineer's existing FEM/BEM solver. Do not claim manufacturability from this transform alone.
