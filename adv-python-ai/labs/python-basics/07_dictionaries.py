# Dictionaries - Key-Value Pairs

# Creating Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

empty_dict = {}
dict_constructor = dict(name="Bob", age=25)

print("=== Creating Dictionaries ===")
print(f"Person: {person}")
print(f"Dict constructor: {dict_constructor}")

# Accessing Values
print("\n=== Accessing Values ===")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Country: {person.get('country', 'USA')}")  # Default value

# Modifying Dictionaries
print("\n=== Modifying Dictionaries ===")
person["email"] = "alice@example.com"
print(f"After adding email: {person}")

person["age"] = 31
print(f"After updating age: {person}")

person.update({"phone": "123-456-7890", "city": "Boston"})
print(f"After update: {person}")

# Removing Items
print("\n=== Removing Items ===")
removed = person.pop("phone")
print(f"Removed: {removed}")
print(f"After pop: {person}")

# Dictionary Methods
print("\n=== Dictionary Methods ===")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Iterating Through Dictionary
print("\n=== Iterating ===")
for key in person:
    print(f"{key}: {person[key]}")

print("\nUsing items():")
for key, value in person.items():
    print(f"{key} = {value}")

# Dictionary Comprehension
print("\n=== Dictionary Comprehension ===")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Nested Dictionaries
print("\n=== Nested Dictionaries ===")
students = {
    "student1": {"name": "John", "grade": "A"},
    "student2": {"name": "Jane", "grade": "B"}
}
print(f"Students: {students}")
print(f"Student1 name: {students['student1']['name']}")

# Dictionary Operations
print("\n=== Dictionary Operations ===")
print(f"Length: {len(person)}")
print(f"'name' in person: {'name' in person}")
print(f"'phone' in person: {'phone' in person}")

# Copying Dictionaries
print("\n=== Copying ===")
person_copy = person.copy()
print(f"Copy: {person_copy}")
