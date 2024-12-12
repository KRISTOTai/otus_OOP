from src.Figure import Figure


class Rectangle(Figure):
    """Вычисление площади и периметра прямоугольника"""

    def __init__(self, side_a: int | float, side_b: int | float):
        if not (side_a > 0 and side_b > 0):
            raise ValueError('Диапазон атрибутов должен быть > 0')
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2
