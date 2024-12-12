from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, side_a: int | float, side_b: int | float):
        if not (side_a > 0 and side_b > 0):
            raise ValueError('Диапазон атрибутов должен быть > 0')
        self.side_a = side_a
        self.side_b = side_b

    @property
    @abstractmethod
    def get_area(self):
        pass

    @property
    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('В метод передана негеометрическая фигура')
        return self.get_area + figure.get_area
