from math import pi
from src.Figure import Figure


class Circle(Figure):
    """Вычисление площади и длины дуги круга"""

    def __init__(self, side_a: int | float):
        super().__init__(side_a, side_a)

    @property
    def area(self):
        return pi * self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 2 * pi
