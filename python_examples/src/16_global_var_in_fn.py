message = "Hey!"


def greet():
    """Simple greeting function."""
    global message  # accessing the global variable message
    message = "Hello"
    return message


output = greet()
print(output)

# printing the global variable
print(message)
