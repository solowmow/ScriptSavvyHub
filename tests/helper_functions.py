# Import necessary modules for testing
import unittest
from src.utils.helper_functions import *

class TestUtils(unittest.TestCase):
    # Basic test cases for utility functions

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10, -3), 7)
        self.assertEqual(add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    # Additional advanced functionalities for testing

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(-3, -4), 12)

    def test_divide(self):
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 0), "Error: Division by zero")

    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(10), 3628800)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, -2), 1/9)
        self.assertEqual(power(4, 5), 1024)

    # New additional functionalities for testing

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average([10, 20, 30, 40, 50]), 30.0)
        self.assertEqual(average([]), 0)  # Testing empty list

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("ScriptSavvyHub"), "buHyvaStpircS")
        self.assertEqual(reverse_string(""), "")  # Testing empty string

    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))  # Testing empty string palindrome

if __name__ == '__main__':
    unittest.main()
# helper_functions.py

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function for exponentiation
def power(base, exponent):
    return base ** exponent

# Function to calculate average of numbers in a list
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Function to reverse a string
def reverse_string(string):
    return string[::-1]

# Function to check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

# Function to find the maximum element in a list
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

# Function to find the minimum element in a list
def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

# Function to convert a string to uppercase
def convert_to_uppercase(string):
    return string.upper()

# Function to count the occurrences of a character in a string
def count_occurrences(string, char):
    return string.count(char)
# helper_functions.py

# ... (Previous functions are retained here)

# Function to find the maximum number in a list
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

# Function to find the minimum number in a list
def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Function to check if a number is odd
def is_odd(number):
    return number % 2 != 0

# Function to calculate the nth term in Fibonacci series
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Function to check if a number is a perfect square
def is_perfect_square(number):
    return number >= 0 and int(number ** 0.5) ** 2 == number

# Function to count the occurrences of a character in a string
def count_character_occurrences(string, char):
    return string.count(char)
# helper_functions.py

# Function to find the maximum number in a list
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

# Function to find the minimum number in a list
def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

# Function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Function to check if a number is odd
def is_odd(n):
    return not is_even(n)

# Function to calculate the Fibonacci series up to n terms
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
