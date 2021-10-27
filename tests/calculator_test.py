"""Import the calculator class"""

from calc.calculator import Calculator


def test_calculator():
    """Testing Calculator's default result is 0"""
    calc1 = Calculator()
    assert calc1.result == 0


def test_get_result():
    """Testing get_result method"""
    calc1 = Calculator()
    calc1.add_number(1, 1)
    assert calc1.get_result() == 0


def test_set_result():
    """Testing set_result method"""
    calc1 = Calculator()
    calc1.set_result(5)
    assert calc1.result == 5


def test_division_by_zero():
    """Testing dividing by zero"""
    calc1 = Calculator()
    calc1.divide_number(0)
