# Engineering Material Database Policy — Acoustic First

Current state: policies only; there is no certified measurement-grade material database.

## Priority order
1. Acoustic medium: sound speed, density, viscosity and temperature dependence where applicable.
2. Diaphragm and surround/spider mechanical properties: density, Young's modulus, Poisson's ratio, damping/loss vs frequency, nonlinear stiffness when measured.
3. Coils: conductor resistance vs temperature, total winding mass, dimensions and winding direction.
4. Magnet and flux-path B-H/remanence/coercivity curves, magnetic permeability and thermal dependence: required for a LATER motor-fitting stage.

## Required record metadata
material_id, vendor and grade (if available), batch/revision, data origin (measurement/datasheet/literature/estimate), source link/document hash, valid temperature and frequency range, SI units, tests and limitations. Curves need abscissa units, sampling and interpolation policy.

## Gating
A placeholder material is metadata, not a validated physical material. No missing value may be silently replaced with an arbitrary numerical guess. Calculations must detect material-property gaps and either stop or label preliminary assumptions and uncertainty prominently.

## Public data
Use material information only with valid reuse rights; customer proprietary records must not be pushed to public GitHub.
