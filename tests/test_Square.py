from src.Square import Square
import pytest


@pytest.mark.parametrize(("side_a", "perimeter"), [(7, 28), (3.12, 12.48)],
                         ids=['integer', 'float'])
def test_square_perimeter(side_a, perimeter):
    s = Square(side_a)
    print(f'Периметр квадрата равен: {s.perimeter}')
    assert s.perimeter == perimeter, f'Расчет периметра квадрата отличается от заданного значения'


@pytest.mark.parametrize(("side_a", "area"), [(5, 25), (3.12, 9.7344)],
                         ids=['integer', 'float'])
def test_square_area(side_a, area):
    s = Square(side_a)
    print(f'Площадь квадрата равна: {s.area}')
    assert s.area == area, f'Расчет площади квадрата отличается от заданного значения'
