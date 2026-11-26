import pytest

from src.metrics.conversion_rate import calculate_conversion


def test_conversion_standard():
    assert calculate_conversion(25, 500) == pytest.approx(5.0)


def test_conversion_zero_visitors():
    with pytest.raises(ValueError, match="Посетители не могут быть нулевыми"):
        calculate_conversion(25, 0)


def test_conversion_zero_conversions():
    assert calculate_conversion(0, 500) == pytest.approx(0.0)


def test_conversion_negative_visitors():
    with pytest.raises(ValueError, match="Посетители не могут быть отрицательными"):
        calculate_conversion(25, -500)


def test_conversion_negative_conversions():
    with pytest.raises(ValueError, match="Конверсии не могут быть отрицательными"):
        calculate_conversion(-5, 500)


def test_conversion_exceeds_visitors():
    with pytest.raises(ValueError, match="Конверсии не могут превышать число посетителей"):
        calculate_conversion(600, 500)


def test_conversion_non_integer_input():
    with pytest.raises(TypeError, match="целыми числами"):
        calculate_conversion(2.5, 500)