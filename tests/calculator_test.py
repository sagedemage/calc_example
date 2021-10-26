"""Import the calculator class"""
from calculator.main import Calculator


def test_calculator():
    """Testing Calculator's default result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_get_result():
    """Testing get_result method"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1


def test_set_result():
    """Testing set_result method"""
    calc = Calculator()
    calc.set_result(5)
    assert calc.result == 5


def test_addition():
    """Testing addition method"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.result == 1


def test_subtract():
    """Testing subtraction method"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.result == -1


def test_multiplication():
    """Testing multiplication method"""
    calc = Calculator()
    calc.multiply_number(1)
    assert calc.result == 0


def test_division():
    """Testing division method"""
    calc = Calculator()
    calc.divide_number(1)
    assert calc.result == 0
