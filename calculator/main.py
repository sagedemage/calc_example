""" content of main.py"""


class Calculator:
    """Calculator class"""
    result = 0

    def get_result(self):
        """Get result fo calculator"""
        return self.result

    def add_number(self, value2):
        """Add a Number"""
        self.result = self.result + value2
        return self.result

    def subtract_number(self, value2):
        """Subtract a Number"""
        self.result = self.result - value2
        return self.result

    def multiply_number(self, value2):
        """Multiply a Number"""
        self.result = self.result * value2
        return self.result

    def divide_number(self, value2):
        """Divide a Number"""
        assert value2 != 0
        self.result = self.result / value2
        return self.result
