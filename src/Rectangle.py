from src.Figure import Figure


class Rectangle(Figure):
    """Вычисление площади и периметра прямоугольника"""

    def __init__(self, side_a: int | float, side_b: int | float):
        super().__init__(side_a, side_b)

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2
