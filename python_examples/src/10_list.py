# List is a collection, where you can keep more than one value in a variable

# =============================================================
# MODULE 1.3d: List Comprehensions
# =============================================================
# A concise Python way to build a new list from an existing sequence.
# General form:
#   [expression for item in iterable]
#   [expression for item in iterable if condition]
#
# Java equivalent: stream().map(...).filter(...).collect(toList())
# But list comprehensions are much simpler to read.
# List - ordered and changeable. Duplicates Allowed

print("=" * 55)
print("MODULE 1.3d: List Comprehensions")
print("=" * 55)


# =============================================================
# Basic: build a list with a transformation
# =============================================================
# print("\n--- squares of 1 to 10 ---")

# # Traditional loop
squares = []

for n in range(1, 12):
    squares.append(n**2)

print(f"Loop result : {squares}")


# # Same thing as a list comprehension - shortcut
cubes = [n**3 for n in range(1, 11)]

print(f"Comprehension: {cubes}")


# # =============================================================
# # Transforming strings
# # =============================================================
print("\n--- title-case names ---")

names = ["alice", "bob", "charlie", "diana"]
titled_names = [name.title() for name in names]
print(f" {titled_names}")


print("\n--- upper-case names longer than 4 chars ---")
long_upper = [name.upper() for name in names if len(name) > 4]
print(f"  {long_upper}")


# # =============================================================
# # Filtering numbers
# # =============================================================
# print("\n--- keep only passing scores (>=60) ---")

scores = [85, 42, 90, 58, 73, 38, 95, 61]
passing = [score for score in scores if score >= 60]
print(f"  All scores : {scores}")
print(f"  Passing    : {passing}")
