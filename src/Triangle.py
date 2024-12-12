from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    """Вычисление площади и периметра у треугольника"""

    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        # Вызов инициализатора родительского класса
        super().__init__(side_a, side_b)
        self.side_c = side_c
        if not (self.side_a + self.side_b > self.side_c and
                self.side_b + self.side_c > self.side_a and
                self.side_c + self.side_a > self.side_b):
            raise ValueError('Треугольника с такими сторонами не существует')

    @property
    def area(self):
        return sqrt((self.perimeter / 2 - self.side_a) * (self.perimeter / 2 - self.side_b) * (
                self.perimeter / 2 - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
