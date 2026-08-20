# =============================================================
# MODULE 2.1d: Sets
# =============================================================
# Unordered, unique values, no duplicates
# Java equivalent: HashSet<T>

# print("=" * 55)
# print("MODULE 2.1d: Sets")
# print("=" * 55)

# # Creating sets
# skills = {"Python", "Java", "SQL", "Python", "Java"}  # duplicates removed!
# print(f"Skills set: {skills}")

# # Adding and removing
# skills.add("Docker")
# skills.add("Python")  # already exists, no change
# print(f"After add('Docker'): {skills}")

# skills.discard("Java")  # safe remove — no error if not found
# print(f"After discard('Java'): {skills}")

# Set operations — very powerful!
team_a = {"Alice", "Bob", "Charlie"}
team_b = {"Bob", "Charlie", "Diana", "Eve"}

print(f"\nTeam A: {team_a}")
print(f"Team B: {team_b}")
print(f"Union (all members):       {team_a | team_b}")  # A ∪ B
print(f"Intersection (both teams): {team_a & team_b}")  # A ∩ B
print(f"Difference (only in A):    {team_a - team_b}")  # A - B
print(f"Symmetric diff (not both): {team_a ^ team_b}")  # XOR

# # Sets are great for removing duplicates from a list
scores_with_duplicates = [85, 90, 85, 72, 90, 68, 72]
unique_scores = list(set(scores_with_duplicates))
print(f"\nOriginal List: {scores_with_duplicates}")
print(f"Unique:   {sorted(unique_scores)}")


# How to access one specific element in a set?
# You can't! Sets are unordered,
# so you can't index into them.
# You can iterate over them, though:

# Converting a set to a list to access elements by index
# is possible, but not recommended if you don't need to.
