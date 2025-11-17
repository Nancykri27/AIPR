"""
A simple calculator module providing basic math operations.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the result of subtracting b from a."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the result of dividing a by b. Handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b
