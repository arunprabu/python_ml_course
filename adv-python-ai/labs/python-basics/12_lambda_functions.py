# Lambda Functions - Anonymous Functions

# Basic Lambda Function
print("=== Basic Lambda Function ===")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

cube = lambda x: x ** 3
print(f"Cube of 3: {cube(3)}")

# Lambda with Multiple Arguments
print("\n=== Multiple Arguments ===")
add = lambda a, b: a + b
print(f"10 + 5 = {add(10, 5)}")

multiply = lambda a, b, c: a * b * c
print(f"2 * 3 * 4 = {multiply(2, 3, 4)}")

# Lambda with Conditional Expression
print("\n=== Lambda with Conditionals ===")
max_num = lambda a, b: a if a > b else b
print(f"Max of 10 and 20: {max_num(10, 20)}")

even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"7 is: {even_or_odd(7)}")
print(f"8 is: {even_or_odd(8)}")

# Lambda with map()
print("\n=== Lambda with map() ===")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Convert to uppercase
words = ["hello", "world", "python"]
uppercase = list(map(lambda x: x.upper(), words))
print(f"\nWords: {words}")
print(f"Uppercase: {uppercase}")

# Lambda with filter()
print("\n=== Lambda with filter() ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Even numbers: {evens}")

# Filter positive numbers
mixed_numbers = [-5, -2, 0, 3, 8, -1, 10]
positives = list(filter(lambda x: x > 0, mixed_numbers))
print(f"\nMixed: {mixed_numbers}")
print(f"Positive: {positives}")

# Lambda with reduce()
print("\n=== Lambda with reduce() ===")
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Sum of {numbers}: {sum_result}")

product = reduce(lambda x, y: x * y, numbers)
print(f"Product of {numbers}: {product}")

# Lambda with sorted()
print("\n=== Lambda with sorted() ===")
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]

# Sort by age
sorted_by_age = sorted(students, key=lambda x: x["age"])
print("Sorted by age:")
for student in sorted_by_age:
    print(f"  {student['name']}: {student['age']}")

# Sort by name
sorted_by_name = sorted(students, key=lambda x: x["name"])
print("\nSorted by name:")
for student in sorted_by_name:
    print(f"  {student['name']}: {student['age']}")

# Lambda in List Comprehension
print("\n=== Lambda in List Comprehension ===")
numbers = [1, 2, 3, 4, 5]
process = lambda x: x ** 2 if x % 2 == 0 else x ** 3
result = [process(x) for x in numbers]
print(f"Numbers: {numbers}")
print(f"Processed: {result}")

# Multiple Lambdas
print("\n=== Multiple Lambdas ===")
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
}

print(f"10 + 5 = {operations['add'](10, 5)}")
print(f"10 - 5 = {operations['subtract'](10, 5)}")
print(f"10 * 5 = {operations['multiply'](10, 5)}")
print(f"10 / 5 = {operations['divide'](10, 5)}")

# Lambda vs Regular Function
print("\n=== Lambda vs Regular Function ===")

# Regular function
def square_regular(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(f"Regular function: {square_regular(6)}")
print(f"Lambda function: {square_lambda(6)}")

# Practical Example: String Manipulation
print("\n=== Practical Example: String Manipulation ===")
names = ["alice", "bob", "charlie", "david"]

# Capitalize and filter names with length > 3
processed_names = list(map(lambda x: x.capitalize(), 
                           filter(lambda x: len(x) > 3, names)))
print(f"Original: {names}")
print(f"Processed (capitalized, len>3): {processed_names}")

# Practical Example: Data Processing
print("\n=== Practical Example: Data Processing ===")
prices = [100, 250, 75, 450, 125]
discount = lambda price: price * 0.9 if price > 200 else price
discounted_prices = list(map(discount, prices))

print("Price comparisons:")
for original, discounted in zip(prices, discounted_prices):
    if original != discounted:
        print(f"  ${original} -> ${discounted:.2f} (10% off)")
    else:
        print(f"  ${original} (no discount)")
