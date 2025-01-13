#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1    # Missing decrement of n in original code
    return result

# Add error handling for command line arguments
if len(sys.argv) != 2:
    print("Usage: script.py <number>")
    sys.exit(1)

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Please provide a valid integer")
