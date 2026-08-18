# =============================================================
# SECTION 6: Numeric Operations and math Module
# =============================================================
import math

a = 17
b = 5

print(f"\nBasic arithmetic with a={a}, b={b}:")
print(f"  a + b  = {a + b}")
print(f"  a - b  = {a - b}")
print(f"  a * b  = {a * b}")
print(f"  a / b  = {a / b}")  # always float in Python 3 (unlike Java!)
print(f"  a // b = {a // b}")  # integer (floor) division
print(f"  a % b  = {a % b}")  # modulo
print(f"  a ** b = {a ** b}")  # power (** replaces Math.pow in Java)

print("*" * 50)

# Compound assignment operators
counter = 0
counter += 1  # same as Java
counter -= 1
counter *= 2
print(f"\ncounter after operations: {counter}")

# NOTE: Python has NO ++ or -- operators (unlike Java)
# Use += 1 or -= 1

# --- math module ---
print(f"\nmath.sqrt(144)      = {math.sqrt(144)}")
print(f"math.ceil(3.2)      = {math.ceil(3.2)}")
print(f"math.floor(3.9)     = {math.floor(3.9)}")
print(f"math.pi             = {math.pi:.5f}")
print(f"math.pow(2, 8)      = {math.pow(2, 8)}")
print(f"math.log(100, 10)   = {math.log(100, 10)}")
print(f"abs(-42)            = {abs(-42)}")  # built-in, no import needed
print(f"round(3.14159, 2)   = {round(3.14159, 2)}")  # built-in
