import pytest


@pytest.fixture(scope='session', autouse=True)
def create_data_for_autouse():
    print('\nНачало тестов')
    yield
    print('\nОкончание тестов')


@pytest.fixture()
def create_data_for_rectangle_perimeter_2():
    a = 5
    b = 7
    yield a, b
