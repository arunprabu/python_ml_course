def create_employee(name, dept, salary=50000, is_active=True):
    """
    name, dept    → positional (required)
    salary        → keyword with default value
    is_active     → keyword with default value
    """
    return {"name": name, "dept": dept, "salary": salary, "is_active": is_active}


# Positional arguments — order matters
emp1 = create_employee("Alice", "Engineering")
print(f"\nemp1: {emp1}")


# Keyword arguments — order doesn't matter
emp2 = create_employee(dept="Marketing", name="Bob", salary=60000)
print(f"emp2: {emp2}")

# Mix of positional and keyword
emp3 = create_employee("Charlie", "Finance", is_active=False, salary=75000)
print(f"emp3: {emp3}")
