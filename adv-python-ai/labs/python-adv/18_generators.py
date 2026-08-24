# Generators - Functions that Yield Values Lazily

# Basic Generator
print("=== Basic Generator ===")
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")
print(f"Third value: {next(gen)}")

# Generator in a Loop
print("\n=== Generator in a Loop ===")
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num, end=" ")
print()

# Generator vs List (Memory Efficiency)
print("\n=== Generator vs List ===")
# List - loads everything in memory
def list_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator - yields one at a time
def generator_squares(n):
    for i in range(n):
        yield i ** 2

import sys
list_result = list_squares(1000)
gen_result = generator_squares(1000)

print(f"List size: {sys.getsizeof(list_result)} bytes")
print(f"Generator size: {sys.getsizeof(gen_result)} bytes")

# Generator Expression (like List Comprehension)
print("\n=== Generator Expression ===")
# List comprehension
squares_list = [x**2 for x in range(10)]
print(f"List: {squares_list}")

# Generator expression (uses parentheses)
squares_gen = (x**2 for x in range(10))
print(f"Generator: {squares_gen}")
print(f"Values: {list(squares_gen)}")

# Infinite Generator
print("\n=== Infinite Generator ===")
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print("First 5 numbers from infinite sequence:")
for i, num in enumerate(gen):
    if i >= 5:
        break
    print(num, end=" ")
print()

# Fibonacci Generator
print("\n=== Fibonacci Generator ===")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("First 10 Fibonacci numbers:")
for i, num in enumerate(fib):
    if i >= 10:
        break
    print(num, end=" ")
print()

# Generator with Send
print("\n=== Generator with Send ===")
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")
gen.close()

# Generator Pipeline
print("\n=== Generator Pipeline ===")
def read_data(n):
    """Generate numbers"""
    for i in range(n):
        yield i

def filter_even(numbers):
    """Filter even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square(numbers):
    """Square the numbers"""
    for num in numbers:
        yield num ** 2

# Chain generators
pipeline = square(filter_even(read_data(10)))
print("Pipeline (even numbers squared):", list(pipeline))

# Generator for File Reading
print("\n=== Generator for File Reading ===")
def read_large_file(file_path):
    """Read file line by line (memory efficient)"""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return

# Create sample file
with open("sample_data.txt", "w") as f:
    for i in range(5):
        f.write(f"Line {i+1}\n")

print("Reading file with generator:")
for line in read_large_file("sample_data.txt"):
    print(f"  {line}")

# Cleanup
import os
os.remove("sample_data.txt")

# Generator for Data Processing
print("\n=== Generator for Data Processing ===")
def process_data(data):
    """Process data in chunks"""
    for item in data:
        # Simulate processing
        processed = item * 2
        yield processed

data = [1, 2, 3, 4, 5]
processor = process_data(data)
print("Processed data:", list(processor))

# Practical Example: Range-like Generator
print("\n=== Practical Example: Custom Range ===")
def my_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

print("Custom range(0, 10, 2):", list(my_range(0, 10, 2)))

# Practical Example: Batch Generator
print("\n=== Practical Example: Batch Generator ===")
def batch_generator(data, batch_size):
    """Yield data in batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(20))
print("Data in batches of 5:")
for batch in batch_generator(data, 5):
    print(f"  {batch}")

# Generator with Exception Handling
print("\n=== Generator with Exception Handling ===")
def safe_divide(numbers, divisor):
    for num in numbers:
        try:
            yield num / divisor
        except ZeroDivisionError:
            yield "Cannot divide by zero"

numbers = [10, 20, 30, 40]
results = safe_divide(numbers, 5)
print("Division results:", list(results))

results_zero = safe_divide(numbers, 0)
print("Division by zero:", list(results_zero))

# Practical Example: Prime Number Generator
print("\n=== Practical Example: Prime Numbers ===")
def prime_generator(limit):
    """Generate prime numbers up to limit"""
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

print(f"Prime numbers up to 30: {list(prime_generator(30))}")

# Yield From (Delegating to Another Generator)
print("\n=== Yield From ===")
def sub_generator():
    yield 1
    yield 2

def main_generator():
    yield "Start"
    yield from sub_generator()
    yield "End"

print("Yield from:", list(main_generator()))
