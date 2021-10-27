""" content of division.py """


class Division:
    """Division class"""

    @staticmethod
    def divide(value_a, value_b):
        result = 0
        """Divide two numbers"""
        try:
            result = value_a / value_b
        except ZeroDivisionError as message:
            mes = message
            print(mes)
        return result
