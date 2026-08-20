# =============================================================
# SECTION 7: Lambda Functions
# =============================================================
# Small, anonymous functions for simple operations
# Java equivalent: lambda expressions  (x) -> x * 2
# Python syntax:   lambda params: expression

double = lambda x: x * 2

print(f"\ndouble(5) = {double(5)}")
# the unexecuted function is stored in the above variable double

add = lambda x, y: x + y
print(f"add(3, 4) = {add(3, 4)}")

# # # Lambda with condition
classify = lambda score: "Pass" if score >= 60 else "Fail"
print(f"classify(75) = {classify(75)}")
print(f"classify(45) = {classify(45)}")

# Lambda shines when used inline with map(), filter(), sorted()
