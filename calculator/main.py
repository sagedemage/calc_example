""" content of main.py"""


class Calculator:
    """Calculator class"""
    result = 0

    def get_result(self):
        """Get result for calculator"""
        return self.result

    def set_result(self, value):
        """Set result for calculator"""
        self.result = value

    def add_number(self, value):
        """Add a Number"""
        self.result = self.result + value
        return self.result

    def subtract_number(self, value):
        """Subtract a Number"""
        self.result = self.result - value
        return self.result

    def multiply_number(self, value):
        """Multiply a Number"""
        self.result = self.result * value
        return self.result

    def divide_number(self, value):
        """Divide a Number"""
        assert value != 0
        self.result = self.result / value
        return self.result
