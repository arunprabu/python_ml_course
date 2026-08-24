# Lists - Ordered, Mutable Collections

# Creating Lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]
list_const = list()

print("=== Creating Lists ===")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")
print(f"Empty list: {list_const}")

# Accessing Elements
print("\n=== Accessing Elements ===")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First 2 fruits: {fruits[0:2]}")

# Modifying Lists
print("\n=== Modifying Lists ===")
fruits.append("grape")
print(f"After append: {fruits}")

fruits.insert(1, "mango")
print(f"After insert: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

popped = fruits.pop()
print(f"Popped item: {popped}")
print(f"After pop: {fruits}")

# List Methods
print("\n=== List Methods ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

numbers.sort()
print(f"Sorted: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

# List Comprehension
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# List Operations
print("\n=== List Operations ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined: {combined}")

repeated = list1 * 3
print(f"Repeated: {repeated}")

print(f"Length: {len(combined)}")
print(f"Max: {max(combined)}")
print(f"Min: {min(combined)}")
print(f"Sum: {sum(combined)}")
