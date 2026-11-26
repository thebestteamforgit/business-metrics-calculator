def calculate_conversion_rate(conversions: float, visitors: float) -> float:
    """Возвращает конверсию в процентах: конверсии / посетители * 100."""
    if visitors == 0:
        raise ValueError("Посетители не могут быть нулевыми")
    return conversions / visitors * 100
