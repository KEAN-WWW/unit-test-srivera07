"""This module defines a simple Calculator class with basic arithmetic operations."""
from app.addition import add
from app.subtraction import subtract
from app.multiplication import multiply
from app.division import divide


class Calculator:
    """This class defines a simple Calculator class with basic arithmetic operations."""
    @staticmethod
    def addition (val1, val2):
        """Return the sum of two numbers."""
        return add(val1, val2)

    @staticmethod
    def subtraction (val1, val2):
        """Return the difference between two numbers."""
        return subtract(val1, val2)

    @staticmethod
    def multiplication (val1, val2):
        """Return the product of two numbers."""
        return multiply(val1, val2)

    @staticmethod
    def division (val1, val2):
        """Return the quotient of two numbers.

                Raises:
                    ZeroDivisionError: If `b` is zero.
                """
        return divide(val1, val2)
