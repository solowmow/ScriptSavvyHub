# ScriptSavvyHub - helper_functions.py

# Function 1: Calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function 2: Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function 3: Reverse a string
def reverse_string(s):
    return s[::-1]

# Function 4: Calculate the square of a number
def square(n):
    return n ** 2

# Function 5: Convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function 6: Calculate the average of numbers in a list
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Function 7: Count the occurrences of a specific element in a list
def count_occurrences(lst, element):
    return lst.count(element)

# Function 8: Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
