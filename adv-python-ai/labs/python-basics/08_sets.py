# Sets - Unordered, Unique Collections

# Creating Sets
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates an empty dict, not set

print("=== Creating Sets ===")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# Set automatically removes duplicates
duplicate_numbers = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"With duplicates removed: {duplicate_numbers}")

# Adding Elements
print("\n=== Adding Elements ===")
fruits.add("grape")
print(f"After add: {fruits}")

fruits.update(["mango", "pineapple"])
print(f"After update: {fruits}")

# Removing Elements
print("\n=== Removing Elements ===")
fruits.remove("banana")  # Raises error if not found
print(f"After remove: {fruits}")

fruits.discard("kiwi")  # No error if not found
print(f"After discard (item not found): {fruits}")

popped = fruits.pop()  # Removes arbitrary element
print(f"Popped: {popped}")
print(f"After pop: {fruits}")

# Set Operations
print("\n=== Set Operations ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union
print(f"\nUnion (|): {set1 | set2}")
print(f"Union method: {set1.union(set2)}")

# Intersection
print(f"\nIntersection (&): {set1 & set2}")
print(f"Intersection method: {set1.intersection(set2)}")

# Difference
print(f"\nDifference (-): {set1 - set2}")
print(f"Difference method: {set1.difference(set2)}")

# Symmetric Difference
print(f"\nSymmetric Difference (^): {set1 ^ set2}")
print(f"Symmetric Difference method: {set1.symmetric_difference(set2)}")

# Set Comparisons
print("\n=== Set Comparisons ===")
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"A is subset of B: {set_a.issubset(set_b)}")
print(f"B is superset of A: {set_b.issuperset(set_a)}")
print(f"A and B are disjoint: {set_a.isdisjoint(set_b)}")

# Frozen Sets (Immutable)
print("\n=== Frozen Sets ===")
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")
print("Frozen sets are immutable and can be used as dictionary keys")

# Set Comprehension
print("\n=== Set Comprehension ===")
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Practical Example
print("\n=== Practical Example: Remove Duplicates ===")
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"Original: {numbers_with_duplicates}")
print(f"Unique: {unique_numbers}")
