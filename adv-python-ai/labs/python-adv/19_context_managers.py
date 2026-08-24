# Context Managers - Managing Resources with 'with' Statement

# Basic Context Manager (File Handling)
print("=== Basic Context Manager ===")
# Without context manager (not recommended)
file = open("temp.txt", "w")
file.write("Hello, World!")
file.close()

# With context manager (recommended)
with open("temp.txt", "w") as file:
    file.write("Hello with context manager!")
# File is automatically closed here

print("File written successfully")

# Creating Custom Context Manager (Class-based)
print("\n=== Custom Context Manager (Class) ===")
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        return False

with FileManager("test.txt", "w") as f:
    f.write("Custom context manager!")

# Creating Context Manager with contextlib
print("\n=== Context Manager with contextlib ===")
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    print(f"Opening {filename}")
    file = open(filename, mode)
    try:
        yield file
    finally:
        print(f"Closing {filename}")
        file.close()

with open_file("test2.txt", "w") as f:
    f.write("Using contextlib decorator!")

# Multiple Context Managers
print("\n=== Multiple Context Managers ===")
with open("source.txt", "w") as source, open("dest.txt", "w") as dest:
    source.write("Source content")
    dest.write("Destination content")

print("Both files written")

# Context Manager for Database Connection
print("\n=== Database Context Manager ===")
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        return False

with DatabaseConnection("my_database") as conn:
    print(f"Using: {conn}")
    print("Executing queries...")

# Context Manager with Exception Handling
print("\n=== Context Manager with Exceptions ===")
class SafeOperation:
    def __enter__(self):
        print("Starting safe operation")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            return True  # Suppress the exception
        print("Operation completed successfully")
        return False

with SafeOperation():
    print("Doing some work...")
    # raise ValueError("Something went wrong")  # Uncomment to test

print("Continuing after context manager")

# Timer Context Manager
print("\n=== Timer Context Manager ===")
import time

@contextmanager
def timer(name):
    start = time.time()
    print(f"[{name}] Starting...")
    yield
    end = time.time()
    print(f"[{name}] Completed in {end - start:.4f} seconds")

with timer("Task 1"):
    time.sleep(0.5)
    print("  Processing...")

# Temporary Directory Context Manager
print("\n=== Temporary Directory Context Manager ===")
import os
import tempfile

@contextmanager
def temporary_directory():
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")
    try:
        yield temp_dir
    finally:
        import shutil
        shutil.rmtree(temp_dir)
        print(f"Removed temporary directory: {temp_dir}")

with temporary_directory() as temp_dir:
    # Create a file in temp directory
    temp_file = os.path.join(temp_dir, "temp.txt")
    with open(temp_file, "w") as f:
        f.write("Temporary data")
    print(f"  Working in: {temp_dir}")

# Suppress Context Manager
print("\n=== Suppress Context Manager ===")
from contextlib import suppress

# Without suppress
try:
    int("abc")
except ValueError:
    print("Caught ValueError (traditional way)")

# With suppress (cleaner)
with suppress(ValueError):
    int("xyz")
print("ValueError suppressed")

# Redirect stdout Context Manager
print("\n=== Redirect stdout ===")
from contextlib import redirect_stdout
import io

print("Normal output")

# Capture output
f = io.StringIO()
with redirect_stdout(f):
    print("This goes to StringIO")
    print("Not printed to console")

output = f.getvalue()
print(f"Captured output: {output.strip()}")

# Lock Context Manager
print("\n=== Lock Context Manager ===")
import threading

class SharedResource:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0
    
    def increment(self):
        with self.lock:
            print(f"Incrementing from {self.value}")
            self.value += 1
            return self.value

resource = SharedResource()
print(f"Final value: {resource.increment()}")

# Practical Example: Configuration Manager
print("\n=== Practical Example: Configuration Manager ===")
@contextmanager
def config_override(key, value):
    """Temporarily override a configuration"""
    config = {"debug": False, "log_level": "INFO"}
    
    old_value = config.get(key)
    config[key] = value
    print(f"Config: {key} = {value}")
    
    try:
        yield config
    finally:
        config[key] = old_value
        print(f"Config restored: {key} = {old_value}")

with config_override("debug", True) as cfg:
    print(f"  Running with debug={cfg['debug']}")

# Practical Example: Transaction Manager
print("\n=== Practical Example: Transaction Manager ===")
class Transaction:
    def __init__(self, name):
        self.name = name
        self.committed = False
    
    def __enter__(self):
        print(f"[{self.name}] Transaction started")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
            return False  # Re-raise exception
    
    def commit(self):
        print(f"[{self.name}] Transaction committed")
        self.committed = True
    
    def rollback(self):
        print(f"[{self.name}] Transaction rolled back")
        self.committed = False

# Successful transaction
with Transaction("Payment") as txn:
    print("  Processing payment...")
    print("  Payment successful")

# Failed transaction
try:
    with Transaction("Refund") as txn:
        print("  Processing refund...")
        raise ValueError("Insufficient funds")
except ValueError:
    print("  Transaction failed")

# Cleanup temporary files
print("\n=== Cleanup ===")
for f in ["temp.txt", "test.txt", "test2.txt", "source.txt", "dest.txt"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"Removed: {f}")
