def calculate_aov(revenue: float, orders: int) -> float:
    """Рассчитывает средний чек по выручке и количеству заказов."""
    if orders == 0:
        raise ValueError("Число заказов не может быть нулевым")
    if orders < 0:
        raise ValueError("Число заказов должно быть положительным")
    if revenue < 0:
        raise ValueError("Выручка не может быть отрицательной")
    return revenue / orders
