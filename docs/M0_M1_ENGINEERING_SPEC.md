# M0/M1 Acoustic-First Engineering Specification

Status: draft, not a validated prediction. Supersedes the earlier magnetic-motor-first M1 specification.

## Stage scope
Create standard acoustic targets, low-frequency small-signal electromechanical/pressure-radiation models and constrained inverse searches. Do not solve magnetic geometry before acoustic feasibility.

## Acoustic target must state
- Target points or curve: frequency in Hz, sound pressure level in dB re 20 µPa (RMS air) with tolerances or constrained bands. Define smoothing, gating, and frequency range where relevant.
- Conditions: acoustic environment, distance to observation point, observation angle, baffle or IEC test fixture, open/closed back and any acoustic loading.
- Electrical drive: explicitly distinguish 2.83 V RMS, 1 W, other specified V/I/P. Avoid treating 2.83 V as universally 1 W.
- Boundaries and options: driver OD, effective radiating area if known, package volume limits, excursion, nominal impedance/Re, operating temperature, tolerances and cost target.
- Provenance: engineering proposal, measured sample, manufacturer datasheet, independently published reference or placeholder. Missing values must remain missing.

## Forward model phase (M1.1)
- Start with linear small-signal electro-mechanical equivalent-circuit response: Re, Le (or Z_e(f)), Mms, Cms, Rms, BL, active radiating area and an appropriate acoustic radiation load.
- Explicitly declare assumptions regarding piston motion, acoustic loading, rear radiation, baffle and source feedback.
- Output impedance, diaphragm velocity/displacement, radiated response/SPL at a documented observation point when physically valid.
- No implied full-band response outside model validity or nonlinear THD.

## Inverse model phase (M1.2)
- Fit acoustic response with a bounded and constrained feasible parameter region; use optimization and sensitivity metrics, not agent guesses.
- Constraints must account for parameter interdependence, realizable cone/support geometry, voltage/current/temperature, motor force vs moving mass/compliance, and maximum stroke.
- A single FR curve cannot uniquely identify BL, Re, Mms and Cms. Return multiple feasible design sets and their risk/reality flags.

## Fitting physical design
- Acoustics -> dynamic parameters -> mechanical structure -> motor parameters (BL, Le, Re) -> detailed magnetic FEA -> updated acoustic response.
- A proposed motor geometry must be returned to the acoustic model, not deemed complete based on BL alone.

## Validation levels
V0 unit/schema/condition checks (CI).
V1 independent analytically solvable cases, including impedance/rigid piston within assumptions.
V2 external solver comparison with a curated model (COMSOL Lumped Loudspeaker Driver is a candidate).
V3 physical driver measurement including SPL and impedance under matched conditions.
Publish achieved/blocked/unverified status for each independently.

## References
- https://www.comsol.com/model/lumped-loudspeaker-driver-12295
- https://doc.comsol.com/6.3/doc/com.comsol.help.models.aco.lumped_loudspeaker_driver/lumped_loudspeaker_driver.html
