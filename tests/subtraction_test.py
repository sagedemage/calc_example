"""Testing Subtraction"""

from calc.operations.subtraction import Subtraction


def test_addition():
    """testing calc result is 0"""
    assert Subtraction.subtract(1, 2) == -1