def calculate_conversion(conversions: int, visitors: int) -> float:
    """Возвращает конверсию воронки в процентах: конверсии / посетители * 100."""
    if not isinstance(conversions, int) or not isinstance(visitors, int):
        raise TypeError("Входные данные должны быть целыми числами")
    if visitors == 0:
        raise ValueError("Посетители не могут быть нулевыми")
    if visitors < 0:
        raise ValueError("Посетители не могут быть отрицательными")
    if conversions < 0:
        raise ValueError("Конверсии не могут быть отрицательными")
    if conversions > visitors:
        raise ValueError("Конверсии не могут превышать число посетителей")
    return conversions / visitors * 100