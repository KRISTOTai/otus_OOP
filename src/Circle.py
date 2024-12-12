from src.Rectangle import Rectangle
from math import pi


class Circle(Rectangle):
    """Вычисление площади и длины дуги круга"""

    def __init__(self, side_a: int | float):
        super().__init__(side_a, side_a)

    @property
    def get_area(self):
        return pi * self.side_a ** 2

    @property
    def get_perimeter(self):
        return self.side_a * 2 * pi
