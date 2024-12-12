from src.Rectangle import Rectangle


class Square(Rectangle):
    """Вычисление площади и периметра у квадрата"""

    def __init__(self, side_a: int | float):
        super().__init__(side_a, side_a)
