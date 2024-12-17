import pytest
from src.Triangle import Triangle


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimeter"),
                         [(5, 3, 7, 15), (5.1, 3.1, 7.1, 15.299999999999999)],
                         ids=['integer', 'float'])
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    print(f'Периметр треугольника: {t.perimeter}')
    assert t.perimeter == perimeter, f'Расчет периметра треугольника отличается от заданного значения'


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(5, 3, 7, 2.3717082451262845), (5.1, 3.1, 7.1, 2.526138357255991)],
                         ids=['integer', 'float'])
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    print(f'Площадь треугольника равна : {t.area}')
    assert t.area == area, f'Расчет площади треугольника отличается от заданного значения'


@pytest.mark.xfail(reason='Треугольника с такими сторонами не существует', raises=ValueError)
def test_triangle_sides_negative():
    t = Triangle(-2, 0, 5)
