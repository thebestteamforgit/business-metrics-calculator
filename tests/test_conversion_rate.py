import pytest

from src.metrics.conversion_rate import calculate_conversion_rate


def test_conversion_rate_standard():
    assert calculate_conversion_rate(25, 500) == pytest.approx(5.0)


def test_conversion_rate_zero_visitors():
    with pytest.raises(ValueError, match="Посетители не могут быть нулевыми"):
        calculate_conversion_rate(25, 0)


def test_conversion_rate_zero_conversions():
    assert calculate_conversion_rate(0, 500) == pytest.approx(0.0)