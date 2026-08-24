# 🐍 Python Advanced – Decorators, Generators & Context Managers

## Table of Contents

1. [Decorators](#decorators)
2. [Generators](#generators)
3. [Context Managers](#context-managers)

---

## Decorators

Decorators are a powerful Python feature that allows you to modify or enhance functions and classes without directly changing their code. They use the `@decorator_name` syntax.

### What are Decorators?

A decorator is a function that takes another function as an argument, adds some functionality, and returns a new function.

```python
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
# Output:
# Something before the function
# Hello!
# Something after the function
```

**Without decorator syntax:**

```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
```

### Function Decorators

#### Basic Decorator

```python
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        result = func()
        print("After function call")
        return result
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")
    return "Done"

result = greet()
print(result)
```

#### Decorator with Arguments

```python
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(5, 3)
greet("Alice", greeting="Hi")
```

#### Preserving Function Metadata

Use `functools.wraps` to preserve the original function's metadata:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet someone by name"""
    return f"Hello, {name}!"

print(greet.__name__)      # greet (not wrapper)
print(greet.__doc__)       # Greet someone by name
```

### Practical Decorator Examples

#### 1. Timing Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Done"

@timer
def calculate_sum(n):
    return sum(range(n))

slow_function()
calculate_sum(1000000)
```

#### 2. Logging Decorator

```python
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(5, 3)
```

#### 3. Retry Decorator

```python
from functools import wraps
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise
                    print(f"Attempt {attempts} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

# Will retry up to 3 times
# result = unreliable_function()
```

#### 4. Cache/Memoization Decorator

```python
from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Much faster with memoization
print(fibonacci(100))

# Built-in alternative (Python 3.2+)
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)
```

#### 5. Authentication/Authorization Decorator

```python
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if not user or not user.get('authenticated'):
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get('user')
            if not user or user.get('role') != role:
                raise PermissionError(f"Role '{role}' required")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_auth
def view_profile(user=None):
    return f"Profile for {user['name']}"

@require_role('admin')
def delete_user(user_id, user=None):
    return f"Deleted user {user_id}"

# Usage
user = {'name': 'Alice', 'authenticated': True, 'role': 'admin'}
print(view_profile(user=user))
print(delete_user(123, user=user))
```

#### 6. Validation Decorator

```python
from functools import wraps

def validate_args(**validators):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function parameter names
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate each argument
            for param_name, validator in validators.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not validator(value):
                        raise ValueError(f"Invalid value for {param_name}: {value}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_args(
    age=lambda x: 0 <= x <= 150,
    name=lambda x: isinstance(x, str) and len(x) > 0
)
def create_user(name, age):
    return f"Created user: {name}, age {age}"

print(create_user("Alice", 25))
# print(create_user("", 25))      # ValueError: Invalid value for name
# print(create_user("Bob", 200))  # ValueError: Invalid value for age
```

### Decorators with Parameters

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
# ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']

# Alternative syntax
def prefix_decorator(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}: {result}"
        return wrapper
    return decorator

@prefix_decorator("[INFO]")
def log_message(msg):
    return msg

print(log_message("System started"))  # [INFO]: System started
```

### Stacking Multiple Decorators

```python
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start:.4f}s")
        return result
    return wrapper

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def add_exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

# Decorators are applied bottom-to-top
@timer
@uppercase
@add_exclamation
def greet(name):
    time.sleep(0.1)
    return f"hello, {name}"

print(greet("Alice"))
# HELLO, ALICE!
# Time: 0.1001s
```

### Class Decorators

Decorators can also be applied to classes:

```python
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
        print("Initializing database...")
        self.connection = "Connected"

db1 = Database()  # Initializing database...
db2 = Database()  # (no initialization)
print(db1 is db2)  # True

# Add methods to a class
def add_repr(cls):
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person)  # Person({'name': 'Alice', 'age': 25})
```

### Method Decorators

#### Built-in Method Decorators

```python
class MyClass:
    class_var = "I'm a class variable"

    def __init__(self, value):
        self.value = value

    # Instance method (default)
    def instance_method(self):
        return f"Instance value: {self.value}"

    # Class method
    @classmethod
    def class_method(cls):
        return f"Class variable: {cls.class_var}"

    # Static method
    @staticmethod
    def static_method(x, y):
        return x + y

    # Property (getter)
    @property
    def value_property(self):
        return self._value

    # Property setter
    @value_property.setter
    def value_property(self, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self._value = value

    # Property deleter
    @value_property.deleter
    def value_property(self):
        del self._value

# Usage
obj = MyClass(10)
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method(5, 3))
```

#### Custom Method Decorator

```python
from functools import wraps

def log_method_call(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Calling {func.__name__} on {self.__class__.__name__} instance")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_method_call
    def add(self, a, b):
        return a + b

    @log_method_call
    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
```

### Decorator Classes

Decorators can also be implemented as classes:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

greet("Alice")  # greet has been called 1 times
greet("Bob")    # greet has been called 2 times
greet("Charlie")  # greet has been called 3 times

# With parameters
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()
# Hello!
# Hello!
# Hello!
```

---

## Generators

Generators are a simple way to create iterators. They use the `yield` keyword instead of `return` and maintain their state between calls.

### What are Generators?

A generator is a function that returns an iterator which we can iterate over (one value at a time).

```python
# Regular function
def get_numbers():
    return [1, 2, 3, 4, 5]

# Generator function
def get_numbers_gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Usage
for num in get_numbers_gen():
    print(num)

# Get the generator object
gen = get_numbers_gen()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

### Why Use Generators?

**Benefits:**

1. **Memory Efficient**: Generate values on-the-fly, don't store entire sequence
2. **Lazy Evaluation**: Values are computed only when needed
3. **Infinite Sequences**: Can represent infinite data streams
4. **Pipeline Processing**: Chain operations efficiently

```python
# Memory comparison
import sys

# List - stores all values in memory
numbers_list = [x**2 for x in range(10000)]
print(f"List size: {sys.getsizeof(numbers_list)} bytes")

# Generator - generates values on demand
numbers_gen = (x**2 for x in range(10000))
print(f"Generator size: {sys.getsizeof(numbers_gen)} bytes")

# List size: 87624 bytes
# Generator size: 128 bytes
```

### Creating Generators

#### Generator Functions

```python
def countdown(n):
    print("Starting countdown")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished")

for num in countdown(5):
    print(num)

# Output:
# Starting countdown
# 5
# 4
# 3
# 2
# 1
# Countdown finished
```

#### Generator Expressions

Similar to list comprehensions but with parentheses:

```python
# List comprehension
squares_list = [x**2 for x in range(10)]

# Generator expression
squares_gen = (x**2 for x in range(10))

# Usage
for square in squares_gen:
    print(square)

# Can be used directly in functions that accept iterables
sum_of_squares = sum(x**2 for x in range(10))
```

### Generator Examples

#### 1. Infinite Sequences

```python
def infinite_counter(start=0):
    count = start
    while True:
        yield count
        count += 1

counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

# Fibonacci sequence
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i, num in enumerate(fib):
    if i >= 10:
        break
    print(num, end=' ')
# 0 1 1 2 3 5 8 13 21 34
```

#### 2. Reading Large Files

```python
def read_large_file(file_path):
    """Generator to read large files line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Memory efficient - only one line in memory at a time
# for line in read_large_file('huge_file.txt'):
#     process(line)

def read_in_chunks(file_path, chunk_size=1024):
    """Read file in chunks"""
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk
```

#### 3. Pipeline Processing

```python
def read_numbers(filename):
    """Read numbers from file"""
    with open(filename, 'r') as f:
        for line in f:
            yield int(line.strip())

def square_numbers(numbers):
    """Square each number"""
    for num in numbers:
        yield num ** 2

def filter_even(numbers):
    """Filter even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

# Chain generators together
# numbers = read_numbers('numbers.txt')
# squared = square_numbers(numbers)
# even = filter_even(squared)
# result = sum(even)

# Or in one line
# result = sum(filter_even(square_numbers(read_numbers('numbers.txt'))))
```

#### 4. Generating Batches

```python
def batch_generator(data, batch_size):
    """Generate batches from data"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(1, 21))
for batch in batch_generator(data, batch_size=5):
    print(batch)

# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
```

#### 5. Permutations and Combinations

```python
def permutations(items):
    """Generate all permutations"""
    n = len(items)
    if n <= 1:
        yield items
    else:
        for i in range(n):
            for perm in permutations(items[:i] + items[i+1:]):
                yield [items[i]] + perm

for perm in permutations([1, 2, 3]):
    print(perm)

# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
```

### Generator Methods

#### send()

Send a value to the generator:

```python
def echo():
    while True:
        value = yield
        if value is not None:
            print(f"Received: {value}")

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")  # Received: Hello
gen.send("World")  # Received: World
```

#### throw()

Throw an exception in the generator:

```python
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        yield "Caught ValueError"

gen = my_generator()
print(next(gen))  # 1
print(gen.throw(ValueError))  # Caught ValueError
```

#### close()

Close the generator:

```python
def my_generator():
    try:
        while True:
            yield "Value"
    finally:
        print("Generator closed")

gen = my_generator()
print(next(gen))  # Value
gen.close()       # Generator closed
# print(next(gen))  # StopIteration
```

### Generator Delegation (yield from)

Python 3.3+ allows delegating to sub-generators:

```python
def generator1():
    yield 1
    yield 2

def generator2():
    yield 3
    yield 4

def combined():
    yield from generator1()
    yield from generator2()
    yield 5

for value in combined():
    print(value)
# 1 2 3 4 5

# Practical example - flatten nested lists
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(list(flatten(nested)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Generator Best Practices

```python
# 1. Use generators for large datasets
def process_large_dataset():
    for item in large_data_generator():
        yield process(item)

# 2. Chain generators for pipelines
result = stage3(stage2(stage1(data)))

# 3. Use generator expressions for simple cases
sum_of_squares = sum(x**2 for x in range(1000000))

# 4. Be careful with multiple iterations
gen = (x for x in range(5))
list1 = list(gen)  # [0, 1, 2, 3, 4]
list2 = list(gen)  # [] - generator exhausted!

# 5. Use itertools for common patterns
from itertools import islice, cycle, chain, count

# Take first 10 items
first_ten = list(islice(infinite_counter(), 10))

# Repeat infinitely
infinite_cycle = cycle([1, 2, 3])

# Chain multiple iterables
combined = chain([1, 2], [3, 4], [5, 6])
```

---

## Context Managers

Context managers provide a way to allocate and release resources precisely when needed. They're commonly used with the `with` statement.

### What are Context Managers?

Context managers ensure that resources are properly cleaned up, even if an error occurs.

```python
# Without context manager
file = open('data.txt', 'r')
try:
    content = file.read()
finally:
    file.close()

# With context manager
with open('data.txt', 'r') as file:
    content = file.read()
# File is automatically closed
```

### Creating Context Managers

#### Using a Class

Implement `__enter__()` and `__exit__()` methods:

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        # Return True to suppress exceptions
        return False

# Usage
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
# Output:
# Opening test.txt
# Closing test.txt
```

#### Using contextlib

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print(f"Opening {filename}")
    file = open(filename, mode)
    try:
        yield file
    finally:
        print(f"Closing {filename}")
        file.close()

# Usage
with file_manager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

### Understanding **exit** Parameters

```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exception type: {exc_type}")
        print(f"Exception value: {exc_val}")
        print(f"Exception traceback: {exc_tb}")
        print("Exiting context")

        # Return True to suppress the exception
        # Return False (or None) to propagate it
        if exc_type is ValueError:
            print("Suppressing ValueError")
            return True
        return False

# Without exception
with MyContext():
    print("Inside context")

# With exception (propagated)
try:
    with MyContext():
        raise RuntimeError("Something went wrong")
except RuntimeError:
    print("Caught RuntimeError")

# With exception (suppressed)
with MyContext():
    raise ValueError("This will be suppressed")
print("Execution continues")
```

### Practical Context Manager Examples

#### 1. Database Connection Manager

```python
from contextlib import contextmanager

class DatabaseConnection:
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.database} on {self.host}")
        # Simulate connection
        self.connection = f"Connection to {self.database}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.database}")
        self.connection = None
        return False

# Usage
with DatabaseConnection('localhost', 'mydb') as conn:
    print(f"Using {conn}")
    # Execute queries...

# Alternative with contextlib
@contextmanager
def database_connection(host, database):
    print(f"Connecting to {database} on {host}")
    connection = f"Connection to {database}"
    try:
        yield connection
    finally:
        print(f"Closing connection to {database}")
```

#### 2. Timer Context Manager

```python
import time
from contextlib import contextmanager

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.4f} seconds")
        return False

# Usage
with Timer():
    time.sleep(1)
    print("Doing some work...")

# With contextlib
@contextmanager
def timer(name="Operation"):
    start = time.time()
    print(f"Starting {name}")
    yield
    elapsed = time.time() - start
    print(f"{name} took {elapsed:.4f} seconds")

with timer("Data processing"):
    time.sleep(0.5)
    # Process data...
```

#### 3. Directory Change Manager

```python
import os
from contextlib import contextmanager

@contextmanager
def change_directory(path):
    current_dir = os.getcwd()
    print(f"Changing directory to {path}")
    os.chdir(path)
    try:
        yield
    finally:
        print(f"Returning to {current_dir}")
        os.chdir(current_dir)

# Usage
print(f"Current directory: {os.getcwd()}")
with change_directory('/tmp'):
    print(f"Inside context: {os.getcwd()}")
    # Work in /tmp...
print(f"After context: {os.getcwd()}")
```

#### 4. Temporary File/Directory Manager

```python
from contextlib import contextmanager
import tempfile
import shutil
import os

@contextmanager
def temporary_directory():
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")
    try:
        yield temp_dir
    finally:
        print(f"Removing temporary directory: {temp_dir}")
        shutil.rmtree(temp_dir)

# Usage
with temporary_directory() as temp_dir:
    # Create files in temp_dir
    file_path = os.path.join(temp_dir, 'test.txt')
    with open(file_path, 'w') as f:
        f.write('Temporary data')
    print(f"Working in {temp_dir}")
# temp_dir is automatically cleaned up
```

#### 5. Lock/Mutex Manager

```python
import threading
from contextlib import contextmanager

class Lock:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        print(f"Acquiring lock by {threading.current_thread().name}")
        self.lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing lock by {threading.current_thread().name}")
        self.lock.release()
        return False

# Usage
lock = Lock()

def worker():
    with lock:
        print(f"Critical section: {threading.current_thread().name}")
        time.sleep(0.1)

threads = [threading.Thread(target=worker) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
```

#### 6. Suppress Exceptions

```python
from contextlib import suppress

# Instead of try-except
try:
    os.remove('file_that_might_not_exist.txt')
except FileNotFoundError:
    pass

# Use suppress
with suppress(FileNotFoundError):
    os.remove('file_that_might_not_exist.txt')

# Multiple exceptions
with suppress(FileNotFoundError, PermissionError):
    os.remove('file.txt')
```

#### 7. Redirect stdout/stderr

```python
from contextlib import redirect_stdout, redirect_stderr
import io

# Capture stdout
f = io.StringIO()
with redirect_stdout(f):
    print("This goes to StringIO")
    print("This too")

output = f.getvalue()
print(f"Captured: {output}")

# Redirect to file
with open('output.txt', 'w') as f:
    with redirect_stdout(f):
        print("This goes to file")
```

#### 8. Resource Pool Manager

```python
from contextlib import contextmanager
from queue import Queue

class ResourcePool:
    def __init__(self, create_resource, max_size=10):
        self.create_resource = create_resource
        self.pool = Queue(maxsize=max_size)
        self.size = 0
        self.max_size = max_size

    @contextmanager
    def acquire(self):
        if self.pool.empty() and self.size < self.max_size:
            resource = self.create_resource()
            self.size += 1
        else:
            resource = self.pool.get()

        try:
            yield resource
        finally:
            self.pool.put(resource)

# Usage
def create_connection():
    return f"Connection-{id(object())}"

pool = ResourcePool(create_connection, max_size=5)

with pool.acquire() as conn:
    print(f"Using {conn}")
```

### Multiple Context Managers

```python
# Multiple with statements
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        content = infile.read()
        outfile.write(content.upper())

# Combined (Python 3.1+)
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())

# Using ExitStack for dynamic number of contexts
from contextlib import ExitStack

filenames = ['file1.txt', 'file2.txt', 'file3.txt']

with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # All files are open here
    for f in files:
        print(f.read())
# All files are automatically closed
```

### contextlib Utilities

```python
from contextlib import (
    contextmanager,
    closing,
    suppress,
    redirect_stdout,
    redirect_stderr,
    ExitStack,
    nullcontext
)

# closing - ensures close() is called
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    content = page.read()

# nullcontext - does nothing, useful for conditional contexts
@contextmanager
def optional_context(condition):
    if condition:
        # Return actual context manager
        return Timer()
    else:
        # Return nullcontext
        return nullcontext()

# ExitStack - manage variable number of contexts
def process_files(*filenames):
    with ExitStack() as stack:
        files = [stack.enter_context(open(f)) for f in filenames]
        # Process files...
```

### Async Context Managers

For async/await code (Python 3.5+):

```python
import asyncio
from contextlib import asynccontextmanager

class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("Connecting to database...")
        await asyncio.sleep(0.1)  # Simulate async connection
        self.connection = "DB Connection"
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        await asyncio.sleep(0.1)  # Simulate async cleanup
        return False

# Usage
async def main():
    async with AsyncDatabaseConnection() as conn:
        print(f"Using {conn}")
        await asyncio.sleep(0.1)

# asyncio.run(main())

# With contextlib
@asynccontextmanager
async def async_timer(name):
    start = time.time()
    print(f"Starting {name}")
    yield
    elapsed = time.time() - start
    print(f"{name} took {elapsed:.4f} seconds")

async def process():
    async with async_timer("Async operation"):
        await asyncio.sleep(1)

# asyncio.run(process())
```

### Context Manager Best Practices

```python
# 1. Always use context managers for resources
with open('file.txt') as f:
    data = f.read()

# 2. Create custom context managers for setup/teardown
@contextmanager
def setup_test_environment():
    # Setup
    print("Setting up test environment")
    yield
    # Teardown
    print("Cleaning up test environment")

# 3. Use suppress for expected exceptions
with suppress(FileNotFoundError):
    os.remove('temp_file.txt')

# 4. Chain multiple context managers
with open('in.txt') as infile, open('out.txt', 'w') as outfile:
    outfile.write(infile.read())

# 5. Use ExitStack for dynamic contexts
with ExitStack() as stack:
    resources = [stack.enter_context(acquire_resource(i)) for i in range(n)]
    # Use resources...

# 6. Handle exceptions appropriately in __exit__
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    # Return False to propagate exceptions (default)
    # Return True only if you know what you're doing
    return False
```

---

## Combining Decorators, Generators, and Context Managers

These advanced features can be combined for powerful patterns:

```python
from functools import wraps
from contextlib import contextmanager
import time

# Decorator that uses a generator-based context manager
@contextmanager
def timing_context():
    start = time.time()
    yield
    print(f"Execution time: {time.time() - start:.4f}s")

def with_timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with timing_context():
            return func(*args, **kwargs)
    return wrapper

@with_timing
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()

# Generator with context manager
@contextmanager
def managed_generator(data):
    print("Setting up generator")
    def gen():
        for item in data:
            yield item
    try:
        yield gen()
    finally:
        print("Cleaning up generator")

with managed_generator([1, 2, 3, 4, 5]) as gen:
    for item in gen:
        print(item)

# Decorator factory using context managers
def with_resource(resource_factory):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with resource_factory() as resource:
                return func(resource, *args, **kwargs)
        return wrapper
    return decorator

@with_resource(lambda: open('data.txt'))
def process_file(file, additional_arg):
    return file.read() + additional_arg
```

---

## Summary

### Decorators

✅ Modify/enhance functions without changing their code  
✅ Use `@decorator_name` syntax  
✅ Common uses: logging, timing, caching, validation, authentication  
✅ Can be stacked and parameterized  
✅ Use `functools.wraps` to preserve metadata

### Generators

✅ Create iterators with `yield` keyword  
✅ Memory efficient - lazy evaluation  
✅ Great for large datasets and infinite sequences  
✅ Use generator expressions for simple cases  
✅ Support `send()`, `throw()`, and `close()` methods  
✅ Use `yield from` for delegation

### Context Managers

✅ Manage resources with setup/cleanup logic  
✅ Use `with` statement for automatic resource management  
✅ Implement `__enter__()` and `__exit__()` methods  
✅ Or use `@contextmanager` decorator  
✅ Common uses: files, locks, connections, temporary resources  
✅ Handle exceptions in `__exit__()` appropriately

### Key Takeaways

1. **Decorators**: Enhance functions/classes without modifying their source
2. **Generators**: Process data streams efficiently without loading everything into memory
3. **Context Managers**: Ensure proper resource acquisition and release
4. **Combine them**: Create powerful, clean, and maintainable code patterns

**Happy Coding! 🐍**
