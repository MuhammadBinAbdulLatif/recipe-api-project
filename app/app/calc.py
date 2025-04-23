""""
Calculator module for performing basic arithmetic operations.
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y
def subtract(x,y):
    """Return the difference of x and y."""
    return x - y
def multiply(x,y):
    """Return the product of x and y."""
    return x * y
def divide(x,y):
    """Return the quotient of x and y."""
    if y == 0:
        raise ValueError('The value cannot be zero')
    else:
        return x / y 