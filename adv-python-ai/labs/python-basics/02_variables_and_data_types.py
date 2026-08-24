# Variables and Data Types

# Numeric Types
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j

print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# String Type
name = "Alice"
message = 'Hello, World!'
multi_line = """This is a
multi-line string"""

print(f"\nString: {name}, Type: {type(name)}")

# Boolean Type
is_active = True
is_completed = False

print(f"\nBoolean: {is_active}, Type: {type(is_active)}")

# None Type
no_value = None

print(f"\nNone Type: {no_value}, Type: {type(no_value)}")

# Type Conversion
num_str = "100"
num_int = int(num_str)
num_float = float(num_str)

print(f"\nOriginal: {num_str} (type: {type(num_str)})")
print(f"To int: {num_int} (type: {type(num_int)})")
print(f"To float: {num_float} (type: {type(num_float)})")
