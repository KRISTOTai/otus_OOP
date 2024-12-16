from src.Rectangle import Rectangle
import pytest


def test_rectangle_perimeter_positive_1():
    r = Rectangle(3, 5)
    print(f'Периметр прямоугольника равен: {r.perimeter}')
    assert r.perimeter == 16, f'Расчет периметра прямоугольника отличается от заданного значения'


def test_rectangle_perimeter_2(create_data_for_rectangle_perimeter_2):
    a, b = create_data_for_rectangle_perimeter_2
    r = Rectangle(a, b)
    print(f'Периметр прямоугольника равен: {r.perimeter}')
    assert r.perimeter == 24, f'Расчет периметра прямоугольника отличается от заданного значения'


@pytest.mark.parametrize(("side_a", "side_b", "area"), [(3, 5, 15), (3.12, 5.18, 16.1616)],
                         ids=['integer', 'float'])
def test_rectangle_area_positive_1(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    print(f'Площадь прямоугольника равна: {r.area}')
    assert r.area == area, f'Расчет площади прямоугольника отличается от заданного значения'


@pytest.mark.skip(reason='Для тренировки')
def test_rectangle_area_positive_2():
    r = Rectangle(3.12, 5.18)
    print(f'Площадь прямоугольника равна: {r.area}')
    assert r.area == 15, f'Расчет площади прямоугольника отличается от заданного значения'
