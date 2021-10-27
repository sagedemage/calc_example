"""Testing Addition"""

from calc.operations.multiplication import Multiplication


def test_multiplication():
    """testing calc result is 0"""
    assert Multiplication.add(1, 2) == 3
