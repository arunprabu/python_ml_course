# =============================================================
# MODULE 1.3a: if, elif, else
# =============================================================
# Same logic as Java, but NO parentheses required, NO curly braces.
# Indentation defines the block.

print("=" * 55)
print("MODULE 1.3a: if, elif, else")
print("=" * 55)


# =============================================================
# Basic if-elif-else
# =============================================================
score = 10

if score >= 90:
    grade = "A"
    remark = "Excellent"
elif score >= 80:
    grade = "B"
    remark = "Good"
elif score >= 70:
    grade = "C"
    remark = "Average"
elif score >= 60:
    grade = "D"
    remark = "Below Average"
else:
    grade = "F"
    remark = "Fail"


print(f"Score: {score} → Grade: {grade} ({remark})")


print("=" * 55)


# =============================================================
# Comparison and logical operators
# =============================================================
# Java: &&  ||  !
# Python: and  or  not

print("\n--- and / or / not ---")

age = 22
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")


# 'or' — at least one condition must be true
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("Office is closed")
else:
    print("Office is open")

# 'not' — inverts a boolean
is_logged_in = False

if not is_logged_in:
    print("Please log in first")


# =============================================================
# Chained comparisons (Python-specific — Java doesn't have this)
# =============================================================
print("\n--- chained comparisons ---")

temperature = 24
if 20 <= temperature <= 30:
    print(f"{temperature}°C is comfortable")

bmi = 22.5
if 18.5 <= bmi < 25.0:
    print(f"BMI {bmi} is in normal range")


# =============================================================
# Ternary expression (conditional expression)
# =============================================================
# Java:   String result = (x > 0) ? "positive" : "non-positive";
# Python: result = "positive" if x > 0 else "non-positive"

print("\n--- ternary expression ---")

marks = 55
result = "Pass" if marks >= 50 else "Fail"
print(f"Marks: {marks} so, the result is {result}")
