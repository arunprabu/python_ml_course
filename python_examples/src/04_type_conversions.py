# # =============================================================
# # SECTION 4: Type Conversion
# # =============================================================

# str -> int
age_str = "25"
age_int = int(age_str)
print(f"\nConverted '{age_str}' (str) to {age_int} (int)")


# str -> float
price_str = "199.99"
price_float = float(price_str)
print(f"Converted '{price_str}' (str) to {price_float} (float)")

# int -> str
roll_no = 42
roll_str = str(roll_no)
print(f"Converted {roll_no} (int) to '{roll_str}' (str)")

# int -> float
marks = 85
marks_float = float(marks)
print(f"Converted {marks} (int) to {marks_float} (float)")


# # bool conversions — useful to know
print(f"\nbool(0) = {bool(0)}")  # False
print(f"bool(1) = {bool(1)}")  # True
print(f"bool('') = {bool('')}")  # False (empty string)
print(f"bool('hi') = {bool('hi')}")  # True (non-empty)

# # Be careful with invalid conversions
try:
    bad = int("hello")  # this will fail
except ValueError as e:
    print(f"\nConversion error: {e}")
