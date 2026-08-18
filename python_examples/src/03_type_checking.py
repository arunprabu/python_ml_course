# =============================================================
# SECTION 3: Type Checking — type() and isinstance()
# =============================================================

score = 95
name = "Alice"
gpa = 3.8
active = True


# type() returns the exact type
print(f"\ntype(score)  = {type(score)}")
print(f"type(name)   = {type(name)}")
print(f"type(gpa)    = {type(gpa)}")
print(f"type(active) = {type(active)}")


print("*" * 50)
# isinstance() checks if variable is an instance of a type
# Preferred over type() for type checking (supports inheritance)
print(f"\nisinstance(score, int)   = {isinstance(score, int)}")
print(f"isinstance(gpa, float)   = {isinstance(gpa, float)}")
print(f"isinstance(name, str)    = {isinstance(name, str)}")

# isinstance() can check multiple types at once
value = 42
print(f"Is int or float? {isinstance(value, (int, float))}")
