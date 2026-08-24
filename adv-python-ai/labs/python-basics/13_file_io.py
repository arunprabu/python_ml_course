# File I/O - Reading and Writing Files

import os

# Writing to a File
print("=== Writing to a File ===")
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Python file I/O is easy!\n")
print("File 'sample.txt' created and written")

# Reading from a File
print("\n=== Reading from a File ===")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading Line by Line
print("=== Reading Line by Line ===")
with open("sample.txt", "r") as file:
    for line_num, line in enumerate(file, start=1):
        print(f"Line {line_num}: {line.strip()}")

# Reading All Lines into a List
print("\n=== Reading All Lines ===")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for line in lines:
        print(f"  {line.strip()}")

# Appending to a File
print("\n=== Appending to a File ===")
with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")
    file.write("Another appended line.\n")
print("Content appended to 'sample.txt'")

# Reading after append
print("\nUpdated content:")
with open("sample.txt", "r") as file:
    print(file.read())

# Writing Multiple Lines
print("=== Writing Multiple Lines ===")
lines_to_write = [
    "Line 1: Python\n",
    "Line 2: JavaScript\n",
    "Line 3: Java\n"
]
with open("languages.txt", "w") as file:
    file.writelines(lines_to_write)
print("File 'languages.txt' created")

# Reading with readline()
print("\n=== Reading with readline() ===")
with open("languages.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")

# File Modes
print("\n=== File Modes ===")
print("'r'  - Read (default)")
print("'w'  - Write (overwrites)")
print("'a'  - Append")
print("'r+' - Read and Write")
print("'w+' - Write and Read (overwrites)")
print("'a+' - Append and Read")
print("'b'  - Binary mode (rb, wb, ab)")

# Working with CSV Files
print("\n=== Working with CSV Files ===")
import csv

# Writing CSV
students_data = [
    ["Name", "Age", "Grade"],
    ["Alice", "20", "A"],
    ["Bob", "22", "B"],
    ["Charlie", "21", "A"]
]

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students_data)
print("CSV file 'students.csv' created")

# Reading CSV
print("\nReading CSV:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  {', '.join(row)}")

# File Operations
print("\n=== File Operations ===")

# Check if file exists
if os.path.exists("sample.txt"):
    print("'sample.txt' exists")
    
    # Get file size
    size = os.path.getsize("sample.txt")
    print(f"File size: {size} bytes")
    
    # Get file info
    print(f"Is file: {os.path.isfile('sample.txt')}")
    print(f"Is directory: {os.path.isdir('sample.txt')}")

# Renaming a file
print("\n=== Renaming File ===")
if os.path.exists("languages.txt"):
    os.rename("languages.txt", "programming_languages.txt")
    print("Renamed 'languages.txt' to 'programming_languages.txt'")

# Exception Handling with Files
print("\n=== Exception Handling ===")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"Error: {e}")

# Binary File Operations
print("\n=== Binary File Operations ===")
data = b"Binary data example"
with open("binary_file.bin", "wb") as file:
    file.write(data)
print("Binary file created")

with open("binary_file.bin", "rb") as file:
    binary_content = file.read()
    print(f"Binary content: {binary_content}")

# Context Manager Benefits
print("\n=== Why use 'with' statement? ===")
print("1. Automatically closes files")
print("2. Handles exceptions properly")
print("3. Cleaner and more readable code")
print("4. Prevents resource leaks")

# Clean up example files
print("\n=== Cleanup ===")
files_to_remove = ["sample.txt", "students.csv", "programming_languages.txt", "binary_file.bin"]
for filename in files_to_remove:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed: {filename}")
