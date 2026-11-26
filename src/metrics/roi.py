def calculate_roi(revenue: float, costs: float) -> float:
    """Возвращает ROI в процентах: (выручка - затраты) / затраты * 100.

    Raises:
        TypeError: если аргументы не являются int или float, включая bool.
        ValueError: если затраты <= 0 или выручка < 0.
    """
    if (
        isinstance(revenue, bool)
        or isinstance(costs, bool)
        or not isinstance(revenue, (int, float))
        or not isinstance(costs, (int, float))
    ):
        raise TypeError("Выручка и затраты должны быть числами")
    if costs == 0:
        raise ValueError("Затраты не могут быть нулевыми")
    if costs < 0:
        raise ValueError("Затраты должны быть положительными")
    if revenue < 0:
        raise ValueError("Выручка не может быть отрицательной")
    return (revenue - costs) / costs * 100
