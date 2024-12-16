import pytest
from src.Circle import Circle


@pytest.mark.parametrize(("side_a", "perimeter"), [(5, 31.41592653589793), (3.12, 19.60353815840031)],
                         ids=['integer', 'float'])
def test_circle_perimeter(side_a, perimeter):
    c = Circle(side_a)
    print(f'Длина дуги равна: {c.perimeter}')
    assert c.perimeter == perimeter, f'Расчет длины дуги окружности отличается от заданного значения'


@pytest.mark.parametrize(("side_a", "area"), [(5, 78.53981633974483), (3.12, 30.581519527104486)],
                         ids=['integer', 'float'])
def test_circle_area(side_a, area):
    c = Circle(side_a)
    print(f'Площадь круга равна : {c.area}')
    assert c.area == area, f'Расчет площади круга отличается от заданного значения'
