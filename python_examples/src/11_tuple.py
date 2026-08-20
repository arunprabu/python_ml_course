# =============================================================
# MODULE 2.1b: Tuples
# =============================================================
# Ordered but IMMUTABLE — cannot be changed after creation
# Use when data should NOT change: useful for coordinates, RGB values, DB records

print("=" * 55)
print("MODULE 2.1b: Tuples")
print("=" * 55)

# Creating tuples
point = (10, 20)


rgb = (255, 255, 0)


student_record = ("Alice", 22, "Computer Science", 3.8)

print(f"Student record: {student_record}")

# Indexing works just like lists
print(f"\nName: {student_record[0]}, GPA: {student_record[3]}")

# # Tuple unpacking — very Pythonic!
name, age, department, gpa = student_record
print(f"Unpacked → Name: {name}, Age: {age}, Dept: {department}, GPA: {gpa}")


# Tuples are faster and use less memory than lists
# Use tuple when data is constant, list when data changes

# This raises an error (tuples are immutable):
try:
    point[0] = 99
except TypeError as e:
    print(f"\nTuple is immutable: {e}")
