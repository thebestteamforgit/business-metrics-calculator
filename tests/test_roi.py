import pytest

from src.metrics.roi import calculate_roi


@pytest.mark.parametrize(
    "revenue, costs, expected",
    [
        (1500, 1000, 50.0),
        (500, 1000, -50.0),
        (0, 1000, -100.0),
    ],
)
def test_roi_calculation(revenue, costs, expected):
    assert calculate_roi(revenue, costs) == pytest.approx(expected)


def test_roi_zero_costs():
    with pytest.raises(
        ValueError,
        match="Затраты не могут быть нулевыми"
    ):
        calculate_roi(1500, 0)


def test_roi_negative_costs():
    with pytest.raises(
        ValueError,
        match="Затраты должны быть положительными"
    ):
        calculate_roi(1500, -1000)


def test_roi_negative_revenue():
    with pytest.raises(
        ValueError,
        match="Выручка не может быть отрицательной"
    ):
        calculate_roi(-1500, 1000)


@pytest.mark.parametrize(
    "revenue, costs",
    [
        ("1500", 1000),
        (1500, "1000"),
        (None, 1000),
        (1500, None),
        (True, 1000),
        (1500, True),
        (False, 1000),
        (1500, False),
    ],
)
def test_roi_invalid_input_types(revenue, costs):
    with pytest.raises(
        TypeError,
        match="Выручка и затраты должны быть числами"
    ):
        calculate_roi(revenue, costs)
