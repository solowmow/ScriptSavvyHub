# main.py - ScriptSavvyHub

# Import necessary modules or define helper functions/constants if needed

# Functionality 1: Reading a file and printing its contents
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Functionality 2: Generating a list of prime numbers
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Functionality 3: Reversing a string
def reverse_string(text):
    return text[::-1]

# ... Add more functionalities (Func 4 to Func 15) ...

if __name__ == "__main__":
    # Example usage of functionalities
    read_file('example.txt')

    limit = 20
    primes_list = generate_primes(limit)
    print(f"Prime numbers up to {limit}: {primes_list}")

    text_to_reverse = "Hello, ScriptSavvyHub!"
    reversed_text = reverse_string(text_to_reverse)
    print(f"Reversed text: {reversed_text}")

    # Call other functionalities here...

    # Add the remaining functionalities here...

# main.py - ScriptSavvyHub

# Functionality 1: Reading a file and printing its contents
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Functionality 2: Generating a list of prime numbers
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Functionality 3: Reversing a string
def reverse_string(text):
    return text[::-1]

# Functionality 4: Checking if a string is a palindrome
def is_palindrome(text):
    return text == text[::-1]

# Functionality 5: Counting words in a string
def count_words(text):
    words = text.split()
    return len(words)

# Functionality 6: Calculating factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Functionality 7: Checking if a number is even or odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Functionality 8: Finding the maximum element in a list
def find_max_element(lst):
    return max(lst)

# Functionality 9: Finding the minimum element in a list
def find_min_element(lst):
    return min(lst)

# Functionality 10: Sorting a list in ascending order
def sort_list_ascending(lst):
    return sorted(lst)

# Functionality 11: Converting temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Functionality 12: Converting temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Functionality 13: Calculating the area of a circle
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

# Functionality 14: Calculating the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Functionality 15: Calculating the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name_
# main.py - ScriptSavvyHub

# Functionality 1: Reading a file and printing its contents
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Functionality 2: Generating a list of prime numbers
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Functionality 3: Reversing a string
def reverse_string(text):
    return text[::-1]

# Functionality 4: Checking if a string is a palindrome
def is_palindrome(text):
    return text == text[::-1]

# Functionality 5: Counting words in a string
def count_words(text):
    words = text.split()
    return len(words)

# Functionality 6: Calculating factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Functionality 7: Checking if a number is even or odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Functionality 8: Finding the maximum element in a list
def find_max_element(lst):
    return max(lst)

# Functionality 9: Finding the minimum element in a list
def find_min_element(lst):
    return min(lst)

# Functionality 10: Sorting a list in ascending order
def sort_list_ascending(lst):
    return sorted(lst)

# Functionality 11: Converting temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Functionality 12: Converting temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Functionality 13: Calculating the area of a circle
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

# Functionality 14: Calculating the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Functionality 15: Calculating the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == "__main__":
    # Example usage of functionalities
    read_file('example.txt')

    limit = 20
    primes_list = generate_primes(limit)
    print(f"Prime numbers up to {limit}: {primes_list}")

    text_to_reverse = "Hello, ScriptSavvyHub!"
    reversed_text = reverse_string(text_to_reverse)
    print(f"Reversed text: {reversed_text}")

    # Add more calls to other functionalities here...
    # For example:
    # print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")
    # print(f"Number of words in 'Lorem ipsum dolor sit amet': {count_words('Lorem ipsum dolor sit amet')}")

    # Call the rest of the functionalities here...

# main.py - ScriptSavvyHub

# Functionality 1: Reading a file and printing its contents
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Functionality 2: Generating a list of prime numbers
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Functionality 3: Reversing a string
def reverse_string(text):
    return text[::-1]

# Functionality 4: Checking if a string is a palindrome
def is_palindrome(text):
    return text == text[::-1]

# Functionality 5: Counting words in a string
def count_words(text):
    words = text.split()
    return len(words)

# Functionality 6: Calculating factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Functionality 7: Checking if a number is even or odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Functionality 8: Finding the maximum element in a list
def find_max_element(lst):
    return max(lst)

# Functionality 9: Finding the minimum element in a list
def find_min_element(lst):
    return min(lst)

# Functionality 10: Sorting a list in ascending order
def sort_list_ascending(lst):
    return sorted(lst)

# Functionality 11: Converting temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Functionality 12: Converting temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Functionality 13: Calculating the area of a circle
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

# Functionality 14: Calculating the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Functionality 15: Calculating the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == "__main__":
    # Example usage of functionalities
    read_file('example.txt')

    limit = 20
    primes_list = generate_primes(limit)
    print(f"Prime numbers up to {limit}: {primes_list}")

    text_to_reverse = "Hello, ScriptSavvyHub!"
    reversed_text = reverse_string(text_to_reverse)
    print(f"Reversed text: {reversed_text}")

    # Add more calls to other functionalities here...
    # For example:
    # print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")
    # print(f"Number of words in 'Lorem ipsum dolor sit amet': {count_words('Lorem ipsum dolor sit amet')}")

    # Call the rest of the functionalities here...
