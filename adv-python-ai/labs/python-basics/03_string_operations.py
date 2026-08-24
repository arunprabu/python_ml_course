# String Operations

# String Creation
text = "Python Programming"

# String Indexing
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")

# String Slicing
print(f"\nFirst 6 characters: {text[0:6]}")
print(f"Last 11 characters: {text[7:]}")
print(f"Every 2nd character: {text[::2]}")

# String Methods
print(f"\nUppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title Case: {text.title()}")

# String Operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\nFull name: {full_name}")

# String Formatting
age = 30
print(f"{first_name} is {age} years old")

# String Methods
sentence = "  Hello World  "
print(f"\nOriginal: '{sentence}'")
print(f"Stripped: '{sentence.strip()}'")
print(f"Replace: {sentence.replace('World', 'Python')}")
print(f"Split: {sentence.split()}")

# String Checking
email = "user@example.com"
print(f"\nContains @: {'@' in email}")
print(f"Starts with 'user': {email.startswith('user')}")
print(f"Ends with '.com': {email.endswith('.com')}")
