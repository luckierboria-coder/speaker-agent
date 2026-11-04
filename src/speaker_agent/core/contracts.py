"""Minimal, solver-independent engineering contracts.

This is a foundation only. It does not perform magnetic or acoustic simulation.
All parameter values are expressed in the SI unit declared by the field.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from math import isfinite


class RunStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass(frozen=True, slots=True)
class ScalarSI:
    """A finite scalar with its explicit SI unit string."""

    value: float
    unit: str

    def __post_init__(self) -> None:
        if not isfinite(self.value):
            raise ValueError("Engineering values must be finite")
        if not self.unit or not self.unit.strip():
            raise ValueError("Engineering values require an SI unit")


@dataclass(frozen=True, slots=True)
class DesignInput:
    """Portable design input envelope; topology-specific checks come later."""

    project_id: str
    topology_id: str
    template_version: str
    parameters: dict[str, ScalarSI] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for name in ("project_id", "topology_id", "template_version"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must be nonempty")
        if any(not key.strip() for key in self.parameters):
            raise ValueError("Parameter names must be nonempty")
