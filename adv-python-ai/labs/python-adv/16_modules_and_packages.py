# Modules and Packages in Python

# ============================================
# 1. Importing Standard Library Modules
# ============================================

# Import entire module
import math
print(f"Pi value: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# Import specific functions
from math import factorial, pow
print(f"Factorial of 5: {factorial(5)}")
print(f"2 to the power 3: {pow(2, 3)}")

# Import with alias
import datetime as dt
now = dt.datetime.now()
print(f"Current time: {now}")

# Import all (not recommended in production)
from math import *
print(f"Using ceil: {ceil(4.3)}")

# ============================================
# 2. Common Standard Library Modules
# ============================================

# random module
import random
print(f"\nRandom integer: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'orange'])}")

# os module - operating system interface
import os
print(f"\nCurrent directory: {os.getcwd()}")
print(f"Path separator: {os.sep}")

# sys module - system-specific parameters
import sys
print(f"\nPython version: {sys.version}")
print(f"Platform: {sys.platform}")

# ============================================
# 3. Creating Your Own Module
# ============================================

# Create a simple module file (mymath.py)
# This would normally be in a separate file
mymath_code = """
# mymath.py - Custom math utilities

def add(a, b):
    '''Add two numbers'''
    return a + b

def multiply(a, b):
    '''Multiply two numbers'''
    return a * b

def power(base, exp):
    '''Calculate base raised to exp'''
    return base ** exp

# Module-level variable
PI = 3.14159
"""

# Write the module file
with open('mymath.py', 'w') as f:
    f.write(mymath_code)

# Now import and use our custom module
import mymath
print(f"\nUsing custom module:")
print(f"Add: {mymath.add(5, 3)}")
print(f"Multiply: {mymath.multiply(4, 7)}")
print(f"PI from module: {mymath.PI}")

# ============================================
# 4. Module Attributes
# ============================================

# Every module has special attributes
print(f"\nModule name: {mymath.__name__}")
print(f"Module file: {mymath.__file__}")

# dir() lists all attributes and functions in a module
print(f"\nModule contents: {dir(mymath)}")

# ============================================
# 5. Package Structure
# ============================================

# Create a package structure
# A package is a directory with __init__.py file
import os

# Create package directory
package_dir = 'mypackage'
if not os.path.exists(package_dir):
    os.makedirs(package_dir)

# Create __init__.py (marks directory as package)
init_code = """
# mypackage/__init__.py
'''My custom package'''

__version__ = '1.0.0'

print("Package initialized!")
"""

with open(f'{package_dir}/__init__.py', 'w') as f:
    f.write(init_code)

# Create submodule: arithmetic.py
arithmetic_code = """
# mypackage/arithmetic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

with open(f'{package_dir}/arithmetic.py', 'w') as f:
    f.write(arithmetic_code)

# Create submodule: geometry.py
geometry_code = """
# mypackage/geometry.py

def area_circle(radius):
    return 3.14159 * radius ** 2

def area_rectangle(length, width):
    return length * width
"""

with open(f'{package_dir}/geometry.py', 'w') as f:
    f.write(geometry_code)

# ============================================
# 6. Importing from Packages
# ============================================

# Import entire package
import mypackage
print(f"\nPackage version: {mypackage.__version__}")

# Import specific module from package
from mypackage import arithmetic
print(f"Add using package: {arithmetic.add(10, 5)}")

# Import specific function from submodule
from mypackage.geometry import area_circle
print(f"Circle area: {area_circle(5)}")

# Import with alias
from mypackage.arithmetic import subtract as sub
print(f"Subtract: {sub(20, 8)}")

# ============================================
# 7. The __name__ Variable
# ============================================

# Create a module that can be both imported and run
runnable_module = """
# runnable.py

def greet(name):
    return f"Hello, {name}!"

# Code that only runs when file is executed directly
if __name__ == '__main__':
    print("Running as main program")
    print(greet("World"))
else:
    print("Module imported")
"""

with open('runnable.py', 'w') as f:
    f.write(runnable_module)

# Import it (will print "Module imported")
import runnable
result = runnable.greet("Python")
print(f"\nUsing imported function: {result}")

# ============================================
# 8. Reload Modules (for development)
# ============================================

# Modules are cached after first import
# To reload a modified module:
import importlib
importlib.reload(mymath)
print("\nModule reloaded")

# ============================================
# 9. Module Search Path
# ============================================

# Python searches for modules in these locations
import sys
print("\nModule search paths:")
for path in sys.path[:3]:  # Show first 3 paths
    print(f"  - {path}")

# ============================================
# 10. Popular Third-Party Packages
# ============================================

# Examples of commonly used packages (install with pip):
# pip install requests numpy pandas matplotlib

# Example usage (commented out as packages may not be installed):
# import requests
# response = requests.get('https://api.github.com')
# print(response.status_code)

# import numpy as np
# array = np.array([1, 2, 3, 4, 5])
# print(array.mean())

print("\n" + "="*50)
print("Common third-party packages:")
print("  - requests: HTTP library")
print("  - numpy: Numerical computing")
print("  - pandas: Data analysis")
print("  - matplotlib: Plotting")
print("  - flask/django: Web frameworks")
print("  - pytest: Testing framework")

# ============================================
# 11. Cleanup
# ============================================

print("\n" + "="*50)
print("Module and Package examples completed!")

# Clean up created files and directories
import shutil

try:
    os.remove('mymath.py')
    os.remove('runnable.py')
    shutil.rmtree('mypackage')
    print("\nCleanup completed!")
except Exception as e:
    print(f"\nCleanup note: {e}")
