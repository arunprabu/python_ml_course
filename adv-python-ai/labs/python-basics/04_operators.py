# Operators in Python

# Arithmetic Operators
a = 10
b = 3

print("=== Arithmetic Operators ===")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison Operators
print("\n=== Comparison Operators ===")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical Operators
x = True
y = False

print("\n=== Logical Operators ===")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# Assignment Operators
print("\n=== Assignment Operators ===")
num = 5
print(f"Initial value: {num}")

num += 3  # num = num + 3
print(f"After += 3: {num}")

num *= 2  # num = num * 2
print(f"After *= 2: {num}")

# Identity Operators
print("\n=== Identity Operators ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list3: {list1 is list3}")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 == list2: {list1 == list2}")

# Membership Operators
print("\n=== Membership Operators ===")
fruits = ["apple", "banana", "orange"]
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")
