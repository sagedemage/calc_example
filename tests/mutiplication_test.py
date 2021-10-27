"""Testing Addition"""

from calc.operations.multiplication import Multiplication


def test_multiplication():
    """Testing multiplication method"""
    assert Multiplication.multiply(1, 2) == 2
