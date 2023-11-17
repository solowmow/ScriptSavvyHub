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

if __name__ == '__main__':
    unittest.main()
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

    # Additional advanced functionalities continued

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(average([2.5, 3.5, 4.5]), 3.5)
        self.assertEqual(average([]), None)

    def test_even_odd_count(self):
        self.assertEqual(even_odd_count([1, 2, 3, 4, 5]), (2, 3))
        self.assertEqual(even_odd_count([2, 4, 6]), (3, 0))
        self.assertEqual(even_odd_count([]), (0, 0))

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("radar"))

    def test_max_min_element(self):
        self.assertEqual(max_element([5, 2, 9, 1]), 9)
        self.assertEqual(min_element([5, 2, 9, 1]), 1)
        self.assertEqual(max_element([]), None)
        self.assertEqual(min_element([]), None)

if __name__ == '__main__':
    unittest.main()
import unittest
from src.utils.helper_functions import *

class TestUtils(unittest.TestCase):
    # Existing test cases for basic operations

    def test_addition(self):
        # ...

    def test_subtraction(self):
        # ...

    # Additional advanced functionalities for testing

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(5))
        self.assertFalse(is_even(-3))

    def test_is_odd(self):
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(-7))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(0))

    def test_gcd(self):
        self.assertEqual(gcd(8, 12), 4)
        self.assertEqual(gcd(17, 5), 1)
        self.assertEqual(gcd(100, 75), 25)
        self.assertEqual(gcd(0, 7), 7)

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(5, 7), 35)
        self.assertEqual(lcm(15, 25), 75)
        self.assertEqual(lcm(1, 10), 10)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci(1), [0])

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(876), 21)
        self.assertEqual(sum_of_digits(0), 0)

if __name__ == '__main__':
    unittest.main()
# Import necessary modules for testing
import unittest
from src.utils.helper_functions import *

class TestUtils(unittest.TestCase):
    # Basic test cases for utility functions
    # (Existing tests for addition, subtraction, and imported functions)

    # Additional advanced functionalities for testing

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(15))

    def test_is_odd(self):
        self.assertTrue(is_odd(7))
        self.assertTrue(is_odd(15))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(10))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(30, 45), 15)
        self.assertEqual(gcd(17, 23), 1)

    def test_lcm(self):
        self.assertEqual(lcm(15, 20), 60)
        self.assertEqual(lcm(7, 13), 91)
        self.assertEqual(lcm(3, 5), 15)

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci(1), [0])

    def test_square_root(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(9), 3.0)

if __name__ == '__main__':
    unittest.main()
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
