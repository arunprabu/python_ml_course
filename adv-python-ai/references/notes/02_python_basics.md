# 🐍 Python Basics – Fundamentals, Data Structures, OOP & Modules

## Table of Contents

1. [Python Fundamentals](#python-fundamentals)
2. [Data Structures](#data-structures)
3. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
4. [Modules and Packages](#modules-and-packages)

---

## Python Fundamentals

### Variables and Data Types

Python is **dynamically typed** – no need to declare variable types explicitly.

#### Basic Data Types

```python
# Numbers
integer_num = 42                    # int
float_num = 3.14                    # float
complex_num = 3 + 4j                # complex

# Strings
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is a
multi-line string"""

# Boolean
is_active = True
is_deleted = False

# None (null equivalent)
empty_value = None

# Type checking
print(type(integer_num))            # <class 'int'>
print(isinstance(float_num, float)) # True
```

#### Type Conversion

```python
# Implicit conversion
x = 10
y = 3.5
result = x + y                      # 13.5 (float)

# Explicit conversion
num_str = "123"
num_int = int(num_str)              # 123
num_float = float(num_str)          # 123.0
str_num = str(456)                  # "456"
bool_val = bool(1)                  # True

# Convert to boolean
print(bool(0))                      # False
print(bool(""))                     # False
print(bool([]))                     # False
print(bool("text"))                 # True
```

### Operators

#### Arithmetic Operators

```python
a, b = 10, 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor Division: 3
print(a % b)    # Modulus: 1
print(a ** b)   # Exponentiation: 1000
```

#### Comparison Operators

```python
x, y = 5, 10

print(x == y)   # Equal: False
print(x != y)   # Not equal: True
print(x < y)    # Less than: True
print(x > y)    # Greater than: False
print(x <= y)   # Less than or equal: True
print(x >= y)   # Greater than or equal: False
```

#### Logical Operators

```python
a, b = True, False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

#### Identity Operators

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)       # True (same object)
print(x is y)       # False (different objects)
print(x == y)       # True (same value)
print(x is not y)   # True
```

#### Membership Operators

```python
fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)        # True
print('grape' not in fruits)    # True
```

### Input and Output

```python
# Output
print("Hello, World!")
print("Value:", 42, "Type:", type(42))
print(f"Formatted: {42}")       # f-strings (Python 3.6+)

# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old")
```

### Control Flow

#### If-Elif-Else Statements

```python
age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Just became an adult")
else:
    print("Adult")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
```

#### Loops

**For Loop:**

```python
# Iterate over a sequence
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Range function
for i in range(5):              # 0 to 4
    print(i)

for i in range(2, 10, 2):       # 2, 4, 6, 8
    print(i)

# Enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterate over dictionary
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(f"{key}: {value}")
```

**While Loop:**

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

**Loop Control:**

```python
# Break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)        # Prints 0-4

# Continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)        # Prints 0, 1, 3, 4

# Else clause (executes if loop completes normally)
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

### Functions

#### Basic Functions

```python
# Simple function
def greet():
    print("Hello!")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)       # 8
```

#### Function Arguments

```python
# Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))                   # Hello, Alice!
print(greet("Bob", "Hi"))               # Hi, Bob!

# Keyword arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe_person(age=30, name="John", city="NYC")

# Variable-length arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))          # 15

# Keyword variable-length arguments (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Boston")

# Combining all
def complex_function(a, b, *args, default=10, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"default={default}")
    print(f"kwargs={kwargs}")

complex_function(1, 2, 3, 4, default=20, x=100, y=200)
```

#### Lambda Functions

```python
# Anonymous functions
square = lambda x: x ** 2
print(square(5))                        # 25

add = lambda x, y: x + y
print(add(3, 7))                        # 10

# Used with map, filter, sorted
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))

# Sorting with lambda
people = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
sorted_people = sorted(people, key=lambda x: x['age'])
```

#### Higher-Order Functions

```python
# Function returning a function
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times_three = multiplier(3)
print(times_three(10))                  # 30

# Function as argument
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, lambda a, b: a + b)
print(result)                           # 8
```

### Exception Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching all exceptions
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")

# Finally clause (always executes)
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Always close the file

# Else clause (executes if no exception)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print("Success!")
    print(result)
finally:
    print("Cleanup")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age too high")
    return True

# Custom exceptions
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if '@' not in email:
        raise InvalidEmailError("Email must contain @")
```

---

## Data Structures

### Lists

**Mutable**, ordered sequences that can contain mixed data types.

```python
# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# Accessing elements
print(numbers[0])           # 1 (first element)
print(numbers[-1])          # 5 (last element)
print(numbers[1:4])         # [2, 3, 4] (slicing)
print(numbers[:3])          # [1, 2, 3]
print(numbers[2:])          # [3, 4, 5]
print(numbers[::2])         # [1, 3, 5] (step)
print(numbers[::-1])        # [5, 4, 3, 2, 1] (reverse)

# Modifying lists
numbers[0] = 10             # Change element
numbers.append(6)           # Add to end
numbers.insert(2, 99)       # Insert at index
numbers.extend([7, 8])      # Add multiple elements
numbers.remove(99)          # Remove specific value
popped = numbers.pop()      # Remove and return last
popped = numbers.pop(0)     # Remove and return at index
numbers.clear()             # Remove all elements

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2    # [1, 2, 3, 4, 5, 6]
repeated = list1 * 3        # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()              # Sort in place
sorted_nums = sorted(numbers)  # Return sorted copy
numbers.reverse()           # Reverse in place
count = numbers.count(1)    # Count occurrences
index = numbers.index(4)    # Find index of value

# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
matrix = [[j for j in range(3)] for i in range(3)]

# Useful functions
print(len(numbers))         # Length
print(min(numbers))         # Minimum
print(max(numbers))         # Maximum
print(sum(numbers))         # Sum
print(any([0, 1, 0]))       # True if any element is True
print(all([1, 1, 1]))       # True if all elements are True
```

### Tuples

**Immutable**, ordered sequences. Faster than lists, used for fixed data.

```python
# Creating tuples
empty_tuple = ()
single = (1,)               # Note the comma
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
nested = ((1, 2), (3, 4))

# Accessing elements (same as lists)
print(numbers[0])           # 1
print(numbers[-1])          # 5
print(numbers[1:4])         # (2, 3, 4)

# Tuple unpacking
x, y, z = (1, 2, 3)
a, *rest, b = (1, 2, 3, 4, 5)  # a=1, rest=[2,3,4], b=5

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
count = numbers.count(2)    # 3
index = numbers.index(3)    # 2

# Why use tuples?
# 1. Immutable (data integrity)
# 2. Faster than lists
# 3. Can be used as dictionary keys
# 4. Multiple return values
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# Named tuples (better than regular tuples)
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)             # 10 20
```

### Sets

**Unordered** collections of **unique** elements. Fast membership testing.

```python
# Creating sets
empty_set = set()           # Note: {} creates empty dict
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}
from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Adding and removing
numbers.add(6)              # Add single element
numbers.update([7, 8, 9])   # Add multiple
numbers.remove(1)           # Remove (raises error if not found)
numbers.discard(1)          # Remove (no error if not found)
numbers.pop()               # Remove and return arbitrary element
numbers.clear()             # Remove all

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2         # {1, 2, 3, 4, 5, 6}
union = set1.union(set2)

intersection = set1 & set2  # {3, 4}
intersection = set1.intersection(set2)

difference = set1 - set2    # {1, 2}
difference = set1.difference(set2)

sym_diff = set1 ^ set2      # {1, 2, 5, 6}
sym_diff = set1.symmetric_difference(set2)

# Subset and superset
subset = {1, 2}
print(subset.issubset(set1))        # True
print(set1.issuperset(subset))      # True
print(set1.isdisjoint(set2))        # False

# Frozen sets (immutable sets)
frozen = frozenset([1, 2, 3])
# Can be used as dictionary keys

# Set comprehension
squares = {x**2 for x in range(10)}
```

### Dictionaries

**Key-value pairs**, unordered (ordered in Python 3.7+), mutable.

```python
# Creating dictionaries
empty_dict = {}
empty_dict = dict()

person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Alternative creation
person = dict(name='John', age=30, city='New York')
pairs = dict([('name', 'John'), ('age', 30)])

# Accessing values
print(person['name'])       # John
print(person.get('age'))    # 30
print(person.get('email', 'N/A'))  # Default value if key not found

# Modifying dictionaries
person['age'] = 31          # Update value
person['email'] = 'john@example.com'  # Add new key-value
del person['city']          # Remove key
removed = person.pop('email')  # Remove and return value
person.update({'age': 32, 'country': 'USA'})  # Update multiple

# Dictionary methods
keys = person.keys()        # dict_keys(['name', 'age'])
values = person.values()    # dict_values(['John', 31])
items = person.items()      # dict_items([('name', 'John'), ('age', 31)])

# Iterating
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

filtered = {k: v for k, v in person.items() if k != 'age'}

# Nested dictionaries
users = {
    'user1': {'name': 'Alice', 'age': 25},
    'user2': {'name': 'Bob', 'age': 30}
}
print(users['user1']['name'])  # Alice

# Merging dictionaries (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2      # {'a': 1, 'b': 3, 'c': 4}

# DefaultDict (auto-creates missing keys)
from collections import defaultdict

word_count = defaultdict(int)
for word in ['apple', 'banana', 'apple']:
    word_count[word] += 1

# Counter (specialized dict for counting)
from collections import Counter

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count = Counter(words)
print(count)                # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(count.most_common(2)) # [('apple', 3), ('banana', 2)]

# OrderedDict (maintains insertion order - less relevant in Python 3.7+)
from collections import OrderedDict

ordered = OrderedDict()
ordered['first'] = 1
ordered['second'] = 2
```

### Strings

**Immutable** sequences of characters.

```python
# Creating strings
single = 'Hello'
double = "World"
triple = '''Multi
line
string'''

# String operations
greeting = "Hello" + " " + "World"  # Concatenation
repeated = "Ha" * 3             # "HaHaHa"
length = len("Hello")           # 5

# Accessing characters
text = "Python"
print(text[0])                  # 'P'
print(text[-1])                 # 'n'
print(text[1:4])                # 'yth'

# String methods
text = "  Hello, World!  "
print(text.upper())             # "  HELLO, WORLD!  "
print(text.lower())             # "  hello, world!  "
print(text.capitalize())        # "  hello, world!  "
print(text.title())             # "  Hello, World!  "
print(text.strip())             # "Hello, World!"
print(text.lstrip())            # "Hello, World!  "
print(text.rstrip())            # "  Hello, World!"

# Searching and replacing
text = "Hello, World!"
print(text.find("World"))       # 7 (index)
print(text.index("World"))      # 7 (raises error if not found)
print(text.count("l"))          # 3
print(text.replace("World", "Python"))  # "Hello, Python!"

# Checking content
text = "Hello123"
print(text.startswith("Hello")) # True
print(text.endswith("123"))     # True
print(text.isalpha())           # False (has numbers)
print(text.isdigit())           # False (has letters)
print(text.isalnum())           # True (alphanumeric)
print("   ".isspace())          # True

# Splitting and joining
text = "apple,banana,cherry"
fruits = text.split(",")        # ['apple', 'banana', 'cherry']
text = " ".join(fruits)         # "apple banana cherry"

# String formatting
name = "Alice"
age = 30

# Old style
text = "Name: %s, Age: %d" % (name, age)

# str.format()
text = "Name: {}, Age: {}".format(name, age)
text = "Name: {n}, Age: {a}".format(n=name, a=age)

# f-strings (Python 3.6+) - recommended
text = f"Name: {name}, Age: {age}"
text = f"Sum: {2 + 2}"
text = f"Name: {name.upper()}"
text = f"Price: {19.99:.2f}"    # Format numbers

# Raw strings (no escape sequences)
path = r"C:\Users\name\file.txt"

# String methods for validation
email = "user@example.com"
print("@" in email)             # True
print(email.split("@"))         # ['user', 'example.com']
```

### Collections Module

```python
from collections import deque, Counter, defaultdict, OrderedDict, namedtuple, ChainMap

# Deque - double-ended queue (efficient append/pop from both ends)
queue = deque([1, 2, 3])
queue.append(4)                 # Add to right
queue.appendleft(0)             # Add to left
queue.pop()                     # Remove from right
queue.popleft()                 # Remove from left
queue.rotate(1)                 # Rotate right

# Counter - counting hashable objects
words = ['apple', 'banana', 'apple', 'cherry']
counter = Counter(words)
print(counter['apple'])         # 2
print(counter.most_common(2))   # [('apple', 2), ('banana', 1)]

# defaultdict - default values for missing keys
dd = defaultdict(list)
dd['fruits'].append('apple')    # No KeyError

# ChainMap - combine multiple dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['b'])               # 2 (from first dict)
```

---

## Object-Oriented Programming (OOP)

### Classes and Objects

```python
# Basic class
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

    # Instance method with parameters
    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old"

    # String representation
    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes
print(dog1.name)                # Buddy
print(dog1.species)             # Canis familiaris

# Calling methods
print(dog1.bark())              # Buddy says woof!
print(dog1.birthday())          # Buddy is now 4 years old
print(dog1)                     # Dog(name=Buddy, age=4)
```

### Class Methods and Static Methods

```python
class MyClass:
    class_variable = "I'm a class variable"

    def __init__(self, value):
        self.value = value

    # Instance method (has access to instance via self)
    def instance_method(self):
        return f"Instance value: {self.value}"

    # Class method (has access to class via cls)
    @classmethod
    def class_method(cls):
        return f"Class variable: {cls.class_variable}"

    # Static method (no access to instance or class)
    @staticmethod
    def static_method():
        return "I'm a static method"

    # Alternative constructor
    @classmethod
    def from_string(cls, string):
        value = int(string)
        return cls(value)

# Usage
obj = MyClass(10)
print(obj.instance_method())        # Instance value: 10
print(MyClass.class_method())       # Class variable: I'm a class variable
print(MyClass.static_method())      # I'm a static method
obj2 = MyClass.from_string("20")    # Alternative constructor
```

### Encapsulation (Private/Protected Attributes)

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._balance = balance         # Protected (convention)
        self.__pin = 1234               # Private (name mangling)

    # Getter
    def get_balance(self):
        return self._balance

    # Setter
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount, pin):
        if pin == self.__pin and amount <= self._balance:
            self._balance -= amount
            return True
        return False

    # Property decorator (Pythonic way)
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value

# Usage
account = BankAccount("John", 1000)
print(account.owner)                # John (public)
print(account._balance)             # 1000 (accessible but not recommended)
# print(account.__pin)              # AttributeError
print(account._BankAccount__pin)    # 1234 (name mangling - not recommended)

# Using properties
print(account.balance)              # 1000
account.balance = 2000
print(account.balance)              # 2000
```

### Inheritance

```python
# Base class (parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def info(self):
        return f"I'm {self.name}"

# Derived class (child)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # Call parent constructor
        self.breed = breed

    # Override parent method
    def speak(self):
        return f"{self.name} says woof!"

    # Add new method
    def fetch(self):
        return f"{self.name} is fetching"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# Usage
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())                  # Buddy says woof!
print(dog.info())                   # I'm Buddy (inherited)
print(dog.fetch())                  # Buddy is fetching
print(cat.speak())                  # Whiskers says meow!

# Check inheritance
print(isinstance(dog, Dog))         # True
print(isinstance(dog, Animal))      # True
print(issubclass(Dog, Animal))      # True
```

### Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "Flying..."

class Swimmable:
    def swim(self):
        return "Swimming..."

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} says quack!"

# Usage
duck = Duck("Donald")
print(duck.speak())                 # Donald says quack!
print(duck.fly())                   # Flying...
print(duck.swim())                  # Swimming...

# Method Resolution Order (MRO)
print(Duck.__mro__)
# Shows the order in which classes are searched for methods
```

### Polymorphism

```python
# Same interface, different implementations
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Polymorphism in action
shapes = [Rectangle(5, 10), Circle(7), Rectangle(3, 4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
```

### Abstract Classes

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def info(self):
        return f"This is a {self.brand}"

class Car(Vehicle):
    def start(self):
        return "Car engine starting..."

    def stop(self):
        return "Car engine stopping..."

# Cannot instantiate abstract class
# vehicle = Vehicle("Generic")  # TypeError

car = Car("Toyota")
print(car.start())              # Car engine starting...
print(car.info())               # This is a Toyota
```

### Special (Magic/Dunder) Methods

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    # Length
    def __len__(self):
        return self.pages

    # Comparison operators
    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    # Addition
    def __add__(self, other):
        total_pages = self.pages + other.pages
        return Book(f"{self.title} & {other.title}",
                   f"{self.author} & {other.author}",
                   total_pages)

    # Indexing
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages

    # Context manager
    def __enter__(self):
        print(f"Opening {self.title}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.title}")

# Usage
book1 = Book("Python 101", "John Doe", 200)
book2 = Book("Python Advanced", "Jane Smith", 350)

print(book1)                    # Python 101 by John Doe
print(len(book1))               # 200
print(book1 < book2)            # True
print(book1['title'])           # Python 101

with book1:
    print("Reading...")
```

### Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"
    hobbies: list = field(default_factory=list)

    def greet(self):
        return f"Hi, I'm {self.name}"

# Automatically generates __init__, __repr__, __eq__, etc.
person1 = Person("Alice", 30)
person2 = Person("Bob", 25, "bob@example.com", ["reading", "coding"])

print(person1)                  # Person(name='Alice', age=30, email='unknown@example.com', hobbies=[])
print(person1.greet())          # Hi, I'm Alice
print(person1 == person2)       # False

# Frozen (immutable) dataclass
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
# p.x = 3.0                     # FrozenInstanceError
```

---

## Modules and Packages

### Modules

A module is a single Python file containing code (functions, classes, variables).

**Creating a module (mymodule.py):**

```python
# mymodule.py
"""This is a sample module"""

PI = 3.14159

def greet(name):
    return f"Hello, {name}!"

class Calculator:
    def add(self, a, b):
        return a + b

_private_var = "I'm private"
```

**Using a module:**

```python
# Import entire module
import mymodule

print(mymodule.PI)
print(mymodule.greet("Alice"))
calc = mymodule.Calculator()

# Import specific items
from mymodule import greet, PI

print(greet("Bob"))
print(PI)

# Import with alias
import mymodule as mm
from mymodule import Calculator as Calc

print(mm.PI)
calc = Calc()

# Import all (not recommended)
from mymodule import *

# Check module location
print(mymodule.__file__)
print(mymodule.__name__)
print(mymodule.__doc__)
```

### Built-in Modules

```python
# Math operations
import math

print(math.pi)                  # 3.141592653589793
print(math.sqrt(16))            # 4.0
print(math.ceil(4.3))           # 5
print(math.floor(4.7))          # 4
print(math.pow(2, 3))           # 8.0

# Random numbers
import random

print(random.random())          # Random float [0.0, 1.0)
print(random.randint(1, 10))    # Random int [1, 10]
print(random.choice(['a', 'b', 'c']))  # Random choice
print(random.shuffle([1, 2, 3, 4]))    # Shuffle list

# Date and time
import datetime

now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# OS operations
import os

print(os.getcwd())              # Current directory
print(os.listdir('.'))          # List files
os.makedirs('new_folder', exist_ok=True)
print(os.path.exists('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('folder'))

# System operations
import sys

print(sys.version)              # Python version
print(sys.platform)             # Platform
print(sys.argv)                 # Command-line arguments
sys.exit()                      # Exit program

# JSON
import json

data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)  # Dict to JSON string
parsed = json.loads(json_string)  # JSON string to dict

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)  # Write to file

# Regular expressions
import re

pattern = r'\d+'                # Match digits
text = "I have 2 apples and 3 oranges"
matches = re.findall(pattern, text)  # ['2', '3']
replaced = re.sub(r'\d+', 'X', text)  # "I have X apples and X oranges"

# Collections
from collections import Counter, defaultdict, deque

# Itertools
from itertools import combinations, permutations, product

print(list(combinations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 3)]
```

### Packages

A package is a directory containing multiple modules and a `__init__.py` file.

**Package structure:**

```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

**mypackage/**init**.py:**

```python
# This file makes the directory a package
# Can be empty or contain initialization code

from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']
__version__ = '1.0.0'
```

**Using a package:**

```python
# Import from package
import mypackage.module1
from mypackage import module1
from mypackage.module1 import function1
from mypackage.subpackage import module3

# Import package
import mypackage
print(mypackage.__version__)
```

### Virtual Environments

Isolate project dependencies:

```bash
# Create virtual environment
python -m venv myenv

# Activate (Unix/macOS)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Install packages
pip install requests pandas numpy

# List installed packages
pip list
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

### pip (Package Manager)

```bash
# Install package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Upgrade package
pip install --upgrade package_name

# Uninstall package
pip uninstall package_name

# Search for packages
pip search keyword

# Show package info
pip show package_name

# List outdated packages
pip list --outdated

# Install from requirements file
pip install -r requirements.txt

# Create requirements file
pip freeze > requirements.txt
```

### The `if __name__ == "__main__"` Idiom

```python
# mymodule.py

def main():
    print("Running as main program")

def helper_function():
    print("I'm a helper function")

# This code only runs when the file is executed directly
# Not when it's imported as a module
if __name__ == "__main__":
    main()
```

```python
# another_file.py
import mymodule  # Won't print "Running as main program"

mymodule.helper_function()  # Will work
```

### Module Search Path

```python
import sys

# Python searches for modules in these locations:
for path in sys.path:
    print(path)

# Add custom path
sys.path.append('/custom/path')

# Environment variable PYTHONPATH also affects search path
```

### Importing Best Practices

```python
# ✅ Good practices
import os
import sys
from collections import Counter
from mypackage import mymodule

# ❌ Avoid
from module import *  # Pollutes namespace
import module1, module2, module3  # Use separate lines

# ✅ Group imports
# 1. Standard library
import os
import sys

# 2. Third-party packages
import requests
import pandas

# 3. Local modules
from mypackage import mymodule

# ✅ Use absolute imports
from mypackage.subpackage import module

# ✅ Conditional imports
try:
    import optional_module
except ImportError:
    optional_module = None

# ✅ Lazy imports (import when needed)
def process_data():
    import pandas as pd  # Only imported when function is called
    return pd.DataFrame()
```

### Creating Installable Packages

**Project structure:**

```
myproject/
    mypackage/
        __init__.py
        module1.py
        module2.py
    tests/
        test_module1.py
    setup.py
    README.md
    LICENSE
```

**setup.py:**

```python
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0',
        'numpy>=1.19.0',
    ],
)
```

**Install locally:**

```bash
# Development mode (editable)
pip install -e .

# Regular install
pip install .

# Build distribution
python setup.py sdist bdist_wheel

# Upload to PyPI
pip install twine
twine upload dist/*
```

---

## Summary

This guide covers:

✅ **Python Fundamentals**: Variables, operators, control flow, functions, exception handling  
✅ **Data Structures**: Lists, tuples, sets, dictionaries, strings, and collections  
✅ **OOP**: Classes, inheritance, polymorphism, encapsulation, abstract classes, dataclasses  
✅ **Modules & Packages**: Creating, importing, built-in modules, virtual environments, pip

### Key Takeaways

- **Lists** are mutable, ordered collections
- **Tuples** are immutable, faster than lists
- **Sets** contain unique elements, fast membership testing
- **Dictionaries** store key-value pairs, O(1) lookup
- **OOP** promotes code reusability and organization
- **Modules** help organize code into separate files
- **Packages** group related modules together
- **Virtual environments** isolate project dependencies

### Next Steps

1. Practice with real projects
2. Learn about decorators and generators
3. Explore asyncio for concurrent programming
4. Study design patterns
5. Contribute to open-source projects
6. Learn testing (unittest, pytest)
7. Explore web frameworks (Django, Flask)
8. Dive into data science (Pandas, NumPy)

**Happy Coding! 🐍**
