# =============================================================
# *args — Variable Positional Arguments
# =============================================================
# *args collects extra positional arguments into a TUPLE
# Useful when you don't know how many arguments will be passed
# Java equivalent: String... args (varargs)


# def calculate_total(*prices):
#     """Sum up any number of prices."""
#     print(f"  Prices received: {prices}   (type: {type(prices).__name__})")
#     return sum(prices)


# print(f"\nTotal: {calculate_total(100, 199, 299, 99)}")
# print(f"Total: {calculate_total(100, 300, 200, 150, 75)}")


# def describe_student(name, *subjects):
#     """Name is positional, remaining args become a tuple."""
#     print(f"\nStudent: {name}")
#     print(f"Enrolled in: {', '.join(subjects)}")
#     print(f"Total subjects: {len(subjects)}")


# describe_student("Alice", "Math", "Python", "DBMS", "Networks")
# describe_student("Bob", "Math", "Physics")


# =============================================================
#  **kwargs — Variable Keyword Arguments
# =============================================================
# **kwargs collects extra keyword arguments into a DICT
# Useful when you want to pass arbitrary named options


def create_profile(name, **details):
    """name is required;
    any other named info is collected in details dict."""
    print(f"\nProfile for: {name}")
    for key, value in details.items():
        print(f"  {key}: {value}")


create_profile("Alice", age=22, dept="CS", gpa=3.8, city="Chennai")
create_profile("Bob", age=25, dept="IT", x=100)


# Combining all: positional, *args, **kwargs
def log_event(event_type, *messages, **metadata):
    print(f"\n[{event_type.upper()}]")
    for msg in messages:
        print(f"  Message: {msg}")
    for k, v in metadata.items():
        print(f"  {k}: {v}")


log_event(
    "error", "File not found", "Retry failed", timestamp="2024-01-15", severity="HIGH"
)
