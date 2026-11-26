import pytest

from src.metrics.average_check import calculate_aov


def test_average_check_standard():
    assert calculate_aov(12000, 40) == pytest.approx(300.0)


def test_average_check_zero_orders():
    with pytest.raises(
        ValueError,
        match="Число заказов не может быть нулевым"
    ):
        calculate_aov(12000, 0)


def test_average_check_negative_orders():
    with pytest.raises(
        ValueError,
        match="Число заказов должно быть положительным"
    ):
        calculate_aov(12000, -5)


def test_average_check_negative_revenue():
    with pytest.raises(
        ValueError,
        match="Выручка не может быть отрицательной"
    ):
        calculate_aov(-12000, 40)


def test_average_check_zero_revenue():
    assert calculate_aov(0, 40) == pytest.approx(0.0)
