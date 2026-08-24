# Tuples - Ordered, Immutable Collections

# Creating Tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma
mixed_tuple = (1, "hello", 3.14, True)
empty_tuple = tuple()

print("=== Creating Tuples ===")
print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Single item: {single_item}")
print(f"Mixed: {mixed_tuple}")
print(f"Empty tuple: {empty_tuple}")

# Accessing Elements
print("\n=== Accessing Elements ===")
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"First 2 colors: {colors[0:2]}")

# Tuple Methods
print("\n=== Tuple Methods ===")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 4: {numbers.index(4)}")

# Tuple Unpacking
print("\n=== Tuple Unpacking ===")
x, y = coordinates
print(f"x = {x}, y = {y}")

name, age, city = ("Alice", 30, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")

# Multiple return values using tuples
def get_person():
    return "Bob", 25, "Boston"

name, age, city = get_person()
print(f"Person: {name}, {age}, {city}")

# Tuple Operations
print("\n=== Tuple Operations ===")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Combined: {combined}")

repeated = tuple1 * 3
print(f"Repeated: {repeated}")

print(f"Length: {len(combined)}")
print(f"Max: {max(combined)}")
print(f"Min: {min(combined)}")

# When to use tuples
print("\n=== Why Use Tuples? ===")
print("1. Immutable - data integrity")
print("2. Faster than lists")
print("3. Can be used as dictionary keys")
print("4. Function multiple return values")

# Named Tuples (from collections)
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(f"\nNamed tuple: {p}")
print(f"Access by name: x={p.x}, y={p.y}")
