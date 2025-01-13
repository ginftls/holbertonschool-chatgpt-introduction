#!/usr/bin/python3
import sys

def factorial(n):
	"""
		Calculate the factorial of a given non-negative integer.
		"""
		if n == 0 or n == 1:
		return 1
		result = 1
		while n > 1:
		result *= n
		n -= 1
		return result

# Main execution block
		if __name__ == "__main__":
# Ensure the user provides exactly one command-line argument
		if len(sys.argv) != 2:
	print("Usage: ./factorial.py <non-negative integer>")
sys.exit(1)

	try:
# Convert the input to an integer
number = int(sys.argv[1])
	if number < 0:
	raise ValueError("Factorial is not defined for negative numbers.")

# Calculate and print the factorial
f = factorial(number)
	print(f"Factorial of {number} is {f}")
	except ValueError as e:
	print(f"Error: {e}")
sys.exit(1)

