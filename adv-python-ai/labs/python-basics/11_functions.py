# Functions - Reusable Code Blocks

# Basic Function
def greet():
    print("Hello, World!")

print("=== Basic Function ===")
greet()

# Function with Parameters
def greet_person(name):
    print(f"Hello, {name}!")

print("\n=== Function with Parameters ===")
greet_person("Alice")
greet_person("Bob")

# Function with Return Value
def add(a, b):
    return a + b

print("\n=== Function with Return ===")
result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with Multiple Returns
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    div_result = a / b if b != 0 else None
    return sum_result, diff_result, prod_result, div_result

print("\n=== Multiple Return Values ===")
s, d, p, dv = calculate(10, 5)
print(f"Sum: {s}, Diff: {d}, Product: {p}, Division: {dv}")

# Default Parameters
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

print("\n=== Default Parameters ===")
greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

# Keyword Arguments
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

print("\n=== Keyword Arguments ===")
display_info(name="Alice", age=30, city="New York")
display_info(age=25, city="Boston", name="Bob")

# *args - Variable Number of Arguments
def sum_all(*numbers):
    total = sum(numbers)
    return total

print("\n=== *args ===")
print(f"Sum: {sum_all(1, 2, 3)}")
print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - Keyword Variable Arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n=== **kwargs ===")
print_details(name="Alice", age=30, city="New York")

# Lambda Functions
print("\n=== Lambda Functions ===")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add_lambda = lambda a, b: a + b
print(f"3 + 4 = {add_lambda(3, 4)}")

# Higher-Order Functions
print("\n=== Higher-Order Functions ===")
numbers = [1, 2, 3, 4, 5]

# map()
squares = list(map(lambda x: x**2, numbers))
print(f"Squares: {squares}")

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# Nested Functions
print("\n=== Nested Functions ===")
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from nested function")

# Recursion
print("\n=== Recursion ===")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Docstrings
def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b

print("\n=== Docstrings ===")
print(f"6 * 7 = {multiply(6, 7)}")
print(f"Function documentation: {multiply.__doc__}")

# Practical Example: Temperature Converter
print("\n=== Practical Example: Temperature Converter ===")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f2 = 77
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F = {temp_c2:.1f}°C")
