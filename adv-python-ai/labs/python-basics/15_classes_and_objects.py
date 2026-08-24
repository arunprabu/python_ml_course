# Classes and Objects - Object-Oriented Programming

# Basic Class Definition
print("=== Basic Class ===")
class Person:
    pass  # Empty class

person1 = Person()
print(f"Created person object: {person1}")

# Class with Attributes
print("\n=== Class with Attributes ===")
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(f"Dog 1: {dog1.name}, Age: {dog1.age}, Species: {dog1.species}")
print(f"Dog 2: {dog2.name}, Age: {dog2.age}, Species: {dog2.species}")

# Class with Methods
print("\n=== Class with Methods ===")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display_info(self):
        print(f"Rectangle: {self.width}x{self.height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

rect = Rectangle(5, 3)
rect.display_info()

# String Representation
print("\n=== String Representation ===")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book = Book("1984", "George Orwell", 328)
print(f"str: {str(book)}")
print(f"repr: {repr(book)}")

# Class Methods and Static Methods
print("\n=== Class Methods and Static Methods ===")
class Calculator:
    # Class attribute
    calculation_count = 0
    
    def __init__(self):
        self.result = 0
    
    # Instance method
    def add(self, a, b):
        Calculator.calculation_count += 1
        self.result = a + b
        return self.result
    
    # Class method
    @classmethod
    def get_calculation_count(cls):
        return cls.calculation_count
    
    # Static method
    @staticmethod
    def is_even(num):
        return num % 2 == 0

calc1 = Calculator()
calc2 = Calculator()

print(f"5 + 3 = {calc1.add(5, 3)}")
print(f"10 + 20 = {calc2.add(10, 20)}")
print(f"Total calculations: {Calculator.get_calculation_count()}")
print(f"Is 10 even? {Calculator.is_even(10)}")

# Inheritance
print("\n=== Inheritance ===")
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

cat = Cat("Whiskers")
dog = Dog("Buddy")

print(cat.speak())
print(dog.speak())

# Method Overriding
print("\n=== Method Overriding ===")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle starting..."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} car starting with ignition..."

car = Car("Toyota", "Camry")
print(car.start())

# Encapsulation (Private Attributes)
print("\n=== Encapsulation ===")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(f"Owner: {account.owner}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: ${account.get_balance()}")

# Properties
print("\n=== Properties ===")
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.celsius = 30
print(f"Updated: {temp.celsius}°C = {temp.fahrenheit}°F")

# Multiple Inheritance
print("\n=== Multiple Inheritance ===")
class Flyable:
    def fly(self):
        return "Flying high!"

class Swimmable:
    def swim(self):
        return "Swimming fast!"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

duck = Duck("Donald")
print(f"{duck.name}: {duck.fly()}")
print(f"{duck.name}: {duck.swim()}")

# Practical Example: Student Management
print("\n=== Practical Example: Student Management ===")
class Student:
    student_count = 0
    
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        Student.student_count += 1
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def __str__(self):
        avg = self.average_grade()
        return f"Student: {self.name}, Age: {self.age}, Average: {avg:.2f}"

student1 = Student("Alice", 20, [85, 90, 92])
student2 = Student("Bob", 22, [78, 82, 88])

print(student1)
print(student2)

student1.add_grade(95)
print(f"\nAfter adding grade:")
print(student1)

print(f"\nTotal students: {Student.student_count}")
