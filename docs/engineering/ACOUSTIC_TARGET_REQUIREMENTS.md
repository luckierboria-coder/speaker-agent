# Acoustic Target Definition and Test Conditions — M0

Purpose: a target is actionable only when the acoustic and electrical measurement context is known.

## Must-have
- An acoustic target ID and declared provenance (proposed, measured, published reference).
- Frequency interval or sampled target frequencies with level/tolerance or a precisely defined alternative objective.
- dB SPL reference pressure and RMS or peak pressure definition.
- Observation distance and angle, driver orientation, and acoustic space/baffle/fixture/back volume.
- Electrical drive type and magnitude. Use explicit V RMS, I RMS or specified electrical power with measured load. 2.83 V is not generally 1 W for a 4-ohm driver.
- Temperature, ambient medium and test window/gating where needed for model-to-measurement comparison.
- Nominal dimensions and power/excursion constraints if known; missing values remain missing, not guessed.
- Target source, author, date and revision.

## First-stage response types
1. Validate: report missing, contradictory or unsupported target conditions.
2. Feasibility: classify target as not assessed until a compatible solver exists.
3. Forward: produce simulated response with solver and assumptions recorded.
4. Inverse: return bounded candidate ranges, uncertainty and objective residuals.
5. Verify: compare using compatible conditions and audited numerical/measurement provenance.

## Scope limitations
- Small-signal lumped piston approximations do not predict breakup modes or distortion by themselves.
- A specified cone velocity in acoustic FEM is not automatically a voltage-driven speaker model.
- A frequency response can correspond to many combinations of Mms/Cms/Rms/BL/Re/Le; never infer a unique physical magnet.

## Example reference
COMSOL Lumped Loudspeaker Driver, Application ID 12295:
https://www.comsol.com/model/lumped-loudspeaker-driver-12295
