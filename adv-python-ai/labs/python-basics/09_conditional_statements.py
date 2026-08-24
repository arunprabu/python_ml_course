# Conditional Statements - if, elif, else

# Basic if statement
print("=== Basic if statement ===")
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
print("\n=== if-else statement ===")
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's pleasant outside")

# if-elif-else statement
print("\n=== if-elif-else statement ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Nested if statements
print("\n=== Nested if statements ===")
username = "admin"
password = "12345"

if username == "admin":
    if password == "12345":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")

# Multiple conditions with and, or
print("\n=== Multiple conditions ===")
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")

# Checking membership
print("\n=== Membership checking ===")
fruits = ["apple", "banana", "orange"]
fruit = "apple"

if fruit in fruits:
    print(f"{fruit} is available")
else:
    print(f"{fruit} is not available")

# Ternary operator (conditional expression)
print("\n=== Ternary operator ===")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Checking truthiness
print("\n=== Truthiness ===")
empty_list = []
if empty_list:
    print("List has items")
else:
    print("List is empty")

name = "Alice"
if name:
    print(f"Hello, {name}")

# Match-case (Python 3.10+)
print("\n=== Match-case statement ===")
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")

# Practical Example: Grade Calculator
print("\n=== Practical Example: Grade Calculator ===")
marks = 78

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A (Excellent)")
elif marks >= 80:
    print("Grade: B (Very Good)")
elif marks >= 70:
    print("Grade: C (Good)")
elif marks >= 60:
    print("Grade: D (Satisfactory)")
elif marks >= 50:
    print("Grade: E (Pass)")
else:
    print("Grade: F (Fail)")
