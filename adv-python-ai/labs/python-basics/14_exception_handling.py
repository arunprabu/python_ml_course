# Exception Handling - try, except, finally

# Basic Exception Handling
print("=== Basic Exception Handling ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Multiple Exception Types
print("\n=== Multiple Exception Types ===")
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid value!")

# Catching Multiple Exceptions
print("\n=== Catching Multiple Exceptions ===")
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Generic Exception Handling
print("\n=== Generic Exception ===")
try:
    result = 10 / 2
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")

# try-except-else
print("\n=== try-except-else ===")
try:
    number = int("123")
except ValueError:
    print("Invalid number")
else:
    print(f"Successfully converted: {number}")
    print("This runs only if no exception occurred")

# try-except-finally
print("\n=== try-except-finally ===")
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always executes, regardless of exceptions")

# Finally with Resource Cleanup
print("\n=== Finally for Cleanup ===")
file = None
try:
    file = open("data.txt", "w")
    file.write("Some data")
    # Simulating an error
    # result = 1 / 0
except Exception as e:
    print(f"Error: {e}")
finally:
    if file:
        file.close()
        print("File closed in finally block")

# Raising Exceptions
print("\n=== Raising Exceptions ===")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation Error: {e}")

# Custom Exceptions
print("\n=== Custom Exceptions ===")
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient balance: {balance}, required: {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")

# Nested try-except
print("\n=== Nested try-except ===")
try:
    print("Outer try block")
    try:
        print("Inner try block")
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner except: Caught division by zero")
        raise  # Re-raise the exception
except ZeroDivisionError:
    print("Outer except: Handling re-raised exception")

# Common Built-in Exceptions
print("\n=== Common Built-in Exceptions ===")
exceptions_demo = {
    "ZeroDivisionError": lambda: 1 / 0,
    "ValueError": lambda: int("abc"),
    "TypeError": lambda: "2" + 2,
    "IndexError": lambda: [1, 2, 3][10],
    "KeyError": lambda: {"a": 1}["b"],
    "FileNotFoundError": lambda: open("nonexistent.txt"),
    "AttributeError": lambda: "string".nonexistent_method()
}

for exc_name, func in exceptions_demo.items():
    try:
        func()
    except Exception as e:
        print(f"{exc_name}: {type(e).__name__}")

# Exception Chaining
print("\n=== Exception Chaining ===")
try:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid operation") from e
except ValueError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")

# Practical Example: Input Validation
print("\n=== Practical Example: Input Validation ===")
def get_positive_number():
    while True:
        try:
            num = int(input("Enter a positive number: "))
            if num <= 0:
                raise ValueError("Number must be positive")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            return None

# Note: Commenting out to avoid blocking execution
# number = get_positive_number()
# if number:
#     print(f"You entered: {number}")

# Best Practices
print("\n=== Exception Handling Best Practices ===")
print("1. Catch specific exceptions first, then generic ones")
print("2. Don't catch all exceptions unless necessary")
print("3. Use finally for cleanup operations")
print("4. Provide meaningful error messages")
print("5. Log exceptions for debugging")
print("6. Don't suppress exceptions silently")
print("7. Use custom exceptions for domain-specific errors")

# Assertion for Debugging
print("\n=== Assertions ===")
age = 25
assert age >= 18, "Age must be 18 or older"
print(f"Age {age} is valid")

try:
    invalid_age = 15
    assert invalid_age >= 18, "Age must be 18 or older"
except AssertionError as e:
    print(f"Assertion failed: {e}")
