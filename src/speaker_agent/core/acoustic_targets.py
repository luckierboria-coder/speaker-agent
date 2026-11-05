"""M0 acoustic target contracts. No acoustic prediction is performed here."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from math import isclose, isfinite


class DriveKind(StrEnum):
    VOLTAGE_RMS = "voltage_rms"
    ELECTRICAL_POWER_W = "electrical_power_w"


class AcousticBoundary(StrEnum):
    FREE_SPACE = "free_space"
    INFINITE_BAFFLE = "infinite_baffle"
    SPECIFIED_FIXTURE = "specified_fixture"


class TargetProvenance(StrEnum):
    PROPOSED = "proposed"
    MEASURED = "measured"
    PUBLISHED_REFERENCE = "published_reference"


def _finite(name: str, value: float) -> None:
    if not isfinite(value):
        raise ValueError(f"{name} must be finite")


@dataclass(frozen=True, slots=True)
class DriveCondition:
    kind: DriveKind
    value: float

    def __post_init__(self) -> None:
        _finite("drive", self.value)
        if self.value <= 0:
            raise ValueError("drive must be positive")
        if self.kind not in DriveKind:
            raise ValueError("unsupported drive kind")


@dataclass(frozen=True, slots=True)
class AcousticCondition:
    distance_m: float
    angle_deg: float
    boundary: AcousticBoundary
    medium: str
    drive: DriveCondition
    reference_pressure_pa: float
    fixture_id: str | None = None

    def __post_init__(self) -> None:
        _finite("distance_m", self.distance_m)
        _finite("angle_deg", self.angle_deg)
        _finite("reference_pressure_pa", self.reference_pressure_pa)
        if self.distance_m <= 0:
            raise ValueError("distance_m must be positive")
        if not -180 <= self.angle_deg <= 180:
            raise ValueError("angle_deg is out of range")
        if self.medium != "air":
            raise ValueError("M0 target contract supports air only")
        if not isclose(self.reference_pressure_pa, 20e-6, rel_tol=1e-9):
            raise ValueError("SPL in air requires 20 µPa RMS reference pressure")
        if self.boundary == AcousticBoundary.SPECIFIED_FIXTURE and not self.fixture_id:
            raise ValueError("specified_fixture requires fixture_id")
        if self.boundary != AcousticBoundary.SPECIFIED_FIXTURE and self.fixture_id:
            raise ValueError("fixture_id requires specified_fixture boundary")


@dataclass(frozen=True, slots=True)
class AcousticTargetPoint:
    frequency_hz: float
    spl_db: float
    tolerance_db: float

    def __post_init__(self) -> None:
        for name in ("frequency_hz", "spl_db", "tolerance_db"):
            _finite(name, getattr(self, name))
        if self.frequency_hz <= 0:
            raise ValueError("frequency_hz must be positive")
        if self.tolerance_db < 0:
            raise ValueError("tolerance_db must not be negative")


@dataclass(frozen=True, slots=True)
class AcousticTarget:
    target_id: str
    provenance: TargetProvenance
    condition: AcousticCondition
    points: tuple[AcousticTargetPoint, ...]
    source_reference: str | None = None

    def __post_init__(self) -> None:
        if not self.target_id.strip():
            raise ValueError("target_id must be nonempty")
        if not self.points:
            raise ValueError("at least one target point is required")
        frequencies = [point.frequency_hz for point in self.points]
        if frequencies != sorted(set(frequencies)):
            raise ValueError("target frequencies must be unique and ascending")
        if self.provenance != TargetProvenance.PROPOSED and not self.source_reference:
            raise ValueError("measured/published targets require source_reference")
