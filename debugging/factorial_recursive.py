#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    The factorial of a number n is the product of all positive integers
    less than or equal to n. For example, factorial(5) = 5 * 4 * 3 * 2 * 1.
    For n = 0, factorial returns 1 by definition.
    Parameters:
        n (int): A non-negative integer for which to calculate the factorial.
                Must be >= 0.
    Returns:
        int: The factorial of n. Returns 1 if n is 0.
    Example:
        >>> factorial(5)
        120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input number from command line arguments
# and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
