import pytest
from calculator import Calculator


@pytest.fixture
def wynik():
    return Calculator(10, 5)


@pytest.fixture
def wynik_zero_div():
    return Calculator(8, 0)


def test_sum(wynik):
    assert wynik.sum() == 15.0


def test_subtract(wynik):
    assert wynik.subtract() == 5.0


def test_multiply(wynik):
    assert wynik.multiply() == 50.0


def test_divide(wynik):
    assert wynik.divide() == 2.0


def test_divide_by_zero(wynik_zero_div):
    assert wynik_zero_div.divide() is None
