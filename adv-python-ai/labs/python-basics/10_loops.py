# Loops - for and while

# For Loop with Range
print("=== For loop with range ===")
for i in range(5):
    print(f"Iteration {i}")

print("\nRange with start and stop:")
for i in range(1, 6):
    print(i, end=" ")

print("\n\nRange with step:")
for i in range(0, 11, 2):
    print(i, end=" ")

# For Loop with Lists
print("\n\n=== For loop with lists ===")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# For Loop with enumerate
print("\n=== For loop with enumerate ===")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\nStarting from index 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# For Loop with Dictionaries
print("\n=== For loop with dictionaries ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

print("Keys:")
for key in person:
    print(key)

print("\nValues:")
for value in person.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")

# While Loop
print("\n=== While loop ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While Loop with condition
print("\n=== While loop with condition ===")
total = 0
number = 1
while total < 50:
    total += number
    number += 1
print(f"Total: {total}, Numbers added: {number - 1}")

# Break Statement
print("\n=== Break statement ===")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")

# Continue Statement
print("\n\n=== Continue statement ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")

# Else with Loops
print("\n\n=== Else with loops ===")
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed successfully")

print("\nWith break (else won't execute):")
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("\nThis won't print")

# Nested Loops
print("\n\n=== Nested loops ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# List Comprehension (Alternative to loops)
print("\n=== List comprehension ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Practical Example: Multiplication Table
print("\n=== Practical Example: Multiplication Table ===")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Practical Example: Find Prime Numbers
print("\n=== Practical Example: Prime Numbers ===")
print("Prime numbers up to 20:")
for num in range(2, 21):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
