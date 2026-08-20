# =============================================================
# MODULE 2.1c: Dictionaries
# =============================================================
# Key-value store, ordered (Python 3.7+)
# Java equivalent: HashMap<K, V>

print("=" * 55)
print("MODULE 2.1c: Dictionaries")
print("=" * 55)


# Creating dictionaries
student = {"name": "Alice", "age": 21, "department": "Computer Science", "gpa": 3.8}

print(f"Student: {student}")

# # Accessing values
print(f"\nName: {student['name']}")
print(f"\nAge: {student['age']}")
# print(f"\nPhone: {student['phone']}")

# # .get() is safer — returns None (or default) if key doesn't exist
print(f"Phone: {student.get('phone')}")  # None
print(f"Phone: {student.get('phone', 'N/A')}")  # 'N/A'

# Adding and updating keys
student["email"] = "alice@example.com"  # add new key
student["age"] = 22  # update existing key
print(f"\nUpdated: {student}")

# # # Removing keys
removed = student.pop("gpa")
print(f"Removed gpa: {removed}")
print(f"After pop: {student}")


# # # Iterating
print("\n--- iterating over dict ---")
for key, value in student.items():
    print(f"  {key}: {value}")

print(f"\nKeys:   {list(student.keys())}")
print(f"Values: {list(student.values())}")

# # Checking if key exists
print(f"\n'name' in student: {'name' in student}")
print(f"'gpa' in student:  {'gpa' in student}")

# # # Dict comprehension
squares_dict = {n: n**2 for n in range(1, 6)}
print(f"\nSquares dict: {squares_dict}")
