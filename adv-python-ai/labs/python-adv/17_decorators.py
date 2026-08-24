# Decorators - Functions that Modify Other Functions

# Basic Decorator
print("=== Basic Decorator ===")
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with Arguments
print("\n=== Decorator with Arguments ===")
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Multiple Decorators
print("\n=== Multiple Decorators ===")
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def get_message(name):
    return f"hello, {name}"

print(get_message("Bob"))

# Decorator with functools.wraps
print("\n=== Decorator with functools.wraps ===")
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """This function is slow"""
    import time
    time.sleep(1)
    return "Done!"

result = slow_function()
print(f"Function name: {slow_function.__name__}")
print(f"Function docstring: {slow_function.__doc__}")

# Class Decorator
print("\n=== Class Decorator ===")
def add_greeting(cls):
    cls.greet = lambda self: f"Hello from {self.name}"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Charlie")
print(person.greet())

# Property Decorator (Getter/Setter)
print("\n=== Property Decorator ===")
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Calculate area"""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")

circle.radius = 10
print(f"New radius: {circle.radius}")
print(f"New area: {circle.area:.2f}")

# Practical Example: Logging Decorator
print("\n=== Practical Example: Logging Decorator ===")
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(x, y):
    return x * y

result1 = add(5, 3)
result2 = multiply(4, 7)

# Practical Example: Validation Decorator
print("\n=== Practical Example: Validation Decorator ===")
def validate_positive(func):
    @wraps(func)
    def wrapper(number):
        if number < 0:
            raise ValueError("Number must be positive")
        return func(number)
    return wrapper

@validate_positive
def square_root(n):
    return n ** 0.5

try:
    print(f"Square root of 16: {square_root(16)}")
    print(f"Square root of -4: {square_root(-4)}")
except ValueError as e:
    print(f"Error: {e}")

# Caching Decorator
print("\n=== Caching Decorator ===")
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci(20): {fibonacci(20)}")
print(f"Cache info: {fibonacci.cache_info()}")

# Singleton Decorator
print("\n=== Singleton Decorator ===")
def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Creating database connection...")
        self.connection = "Connected"

db1 = Database()
db2 = Database()
print(f"db1 is db2: {db1 is db2}")  # True - same instance
