"""Validate target metadata; these are NOT physical simulation tests."""

import pytest

from speaker_agent.core.acoustic_targets import (
    AcousticBoundary,
    AcousticCondition,
    AcousticTarget,
    AcousticTargetPoint,
    DriveCondition,
    DriveKind,
    TargetProvenance,
)


def valid_condition() -> AcousticCondition:
    # Synthetic test fixture, not an engineering measurement.
    return AcousticCondition(
        distance_m=1.0,
        angle_deg=0.0,
        boundary=AcousticBoundary.INFINITE_BAFFLE,
        medium="air",
        drive=DriveCondition(DriveKind.VOLTAGE_RMS, 2.83),
        reference_pressure_pa=20e-6,
    )


def test_proposed_target_is_structured() -> None:
    target = AcousticTarget(
        target_id="synthetic-test-only",
        provenance=TargetProvenance.PROPOSED,
        condition=valid_condition(),
        points=(AcousticTargetPoint(100.0, 82.0, 3.0),),
    )
    assert target.condition.drive.kind is DriveKind.VOLTAGE_RMS


def test_missing_reference_for_published_target_is_rejected() -> None:
    with pytest.raises(ValueError, match="source_reference"):
        AcousticTarget(
            target_id="ref",
            provenance=TargetProvenance.PUBLISHED_REFERENCE,
            condition=valid_condition(),
            points=(AcousticTargetPoint(100.0, 82.0, 3.0),),
        )


def test_missing_fixture_details_are_rejected() -> None:
    with pytest.raises(ValueError, match="fixture_id"):
        AcousticCondition(
            distance_m=1,
            angle_deg=0,
            boundary=AcousticBoundary.SPECIFIED_FIXTURE,
            medium="air",
            drive=DriveCondition(DriveKind.VOLTAGE_RMS, 1),
            reference_pressure_pa=20e-6,
        )


def test_reference_pressure_is_explicit() -> None:
    with pytest.raises(ValueError, match="20 µPa"):
        AcousticCondition(
            distance_m=1,
            angle_deg=0,
            boundary=AcousticBoundary.FREE_SPACE,
            medium="air",
            drive=DriveCondition(DriveKind.VOLTAGE_RMS, 1),
            reference_pressure_pa=1.0,
        )


def test_invalid_curve_order_is_rejected() -> None:
    with pytest.raises(ValueError, match="ascending"):
        AcousticTarget(
            target_id="synthetic-test-only",
            provenance=TargetProvenance.PROPOSED,
            condition=valid_condition(),
            points=(
                AcousticTargetPoint(1000, 80, 2),
                AcousticTargetPoint(100, 81, 2),
            ),
        )


def test_negative_drive_and_negative_tolerance_rejected() -> None:
    with pytest.raises(ValueError, match="drive must be positive"):
        DriveCondition(DriveKind.ELECTRICAL_POWER_W, -1)
    with pytest.raises(ValueError, match="tolerance_db"):
        AcousticTargetPoint(1000, 80, -1)


def test_fixture_id_only_with_fixture_boundary() -> None:
    with pytest.raises(ValueError, match="fixture_id requires"):
        AcousticCondition(
            distance_m=1,
            angle_deg=0,
            boundary=AcousticBoundary.FREE_SPACE,
            medium="air",
            drive=DriveCondition(DriveKind.VOLTAGE_RMS, 1),
            reference_pressure_pa=20e-6,
            fixture_id="some-fixture",
        )
