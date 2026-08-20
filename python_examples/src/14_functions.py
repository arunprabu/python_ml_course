# TODO: explore how to mention the return type


def greet(name: str):
    """Simple greeting function."""
    return f"Hello, {name}!"


message = greet("Alice")
print(message)


# the position of the params doensn't matter in the following
def add(a: int, b: int) -> int:
    print(f"a : {a} and b: {b}")
    return a + b


output = add(10, 20)
print(output)
