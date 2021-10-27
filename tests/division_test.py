"""Testing Addition"""

from calc.operations.division import Division


def test_division():
    """Testing addition method"""
    assert Division.divide(4, 2) == 2
    assert Division.divide(2, 0) == 0
