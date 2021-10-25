""" content of calculator.py#"""
from calculator.main import inc


def test_answer():
    """This tests the function"""
    assert inc(2) == 3


def test_spam():
    """This tests the funciton
    This function runs again to make
    sure the result is the same as
    the previous one"""
    assert inc(2) == 3
