"""M0 contract smoke tests. These tests do not verify any solver physics."""

import pytest

from speaker_agent.core.contracts import DesignInput, RunStatus, ScalarSI


def test_design_input_accepts_explicit_si_values() -> None:
    design = DesignInput(
        project_id="reference-motor-001",
        topology_id="moving_coil_axisymmetric",
        template_version="0.1",
        parameters={"gap_height": ScalarSI(value=0.004, unit="m")},
    )
    assert design.parameters["gap_height"].value == pytest.approx(0.004)
    assert RunStatus.SUCCEEDED.value == "succeeded"


@pytest.mark.parametrize("bad_value", [float("nan"), float("inf"), -float("inf")])
def test_engineering_value_rejects_nonfinite_inputs(bad_value: float) -> None:
    with pytest.raises(ValueError, match="finite"):
        ScalarSI(value=bad_value, unit="m")


def test_engineering_value_requires_unit() -> None:
    with pytest.raises(ValueError, match="SI unit"):
        ScalarSI(value=1.0, unit="")


def test_design_requires_project_identity() -> None:
    with pytest.raises(ValueError, match="project_id"):
        DesignInput(project_id="", topology_id="test", template_version="0.1")
