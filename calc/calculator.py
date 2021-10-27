""" content of calculator.py"""
from calc.operations.subtraction import Subtraction
from calc.operations.addition import Addition
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculator:
    """Calculator class"""
    result = 0

    def get_result(self):
        """Get result for calculator"""
        return self.result

    def set_result(self, value):
        """Set result for calculator"""
        self.result = value

    @staticmethod
    def add_number(value_a, value_b):
        """adds two numbers"""
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_number(value_a, value_b):
        """Subtract a Number"""
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def multiply_number(value_a, value_b):
        """Multiply a Number"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_number(value_a, value_b):
        """Divide a Number"""
        return Division.divide(value_a, value_b)
