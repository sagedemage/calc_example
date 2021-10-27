"""Testing Addition"""

from calc.operations.addition import Addition


def test_addition():
    """Testing addition method"""
    assert Addition.add(1, 2) == 3
