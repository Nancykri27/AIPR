"""
Calculator Module
-----------------
This module provides basic arithmetic operations: addition, subtraction,
multiplication, and division. It demonstrates function documentation using
NumPy-style docstrings.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float or int
        The first number.
    b : float or int
        The second number.

    Returns
    -------
    float or int
        The sum of `a` and `b`.
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float or int
        The number to subtract from.
    b : float or int
        The number to subtract.

    Returns
    -------
    float or int
        The result of `a - b`.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float or int
        The first value.
    b : float or int
        The second value.

    Returns
    -------
    float or int
        The product of `a` and `b`.
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : float or int
        The numerator.
    b : float or int
        The denominator.

    Returns
    -------
    float or str
        The result of `a / b`, or an error message if dividing by zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b
