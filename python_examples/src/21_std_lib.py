# =============================================================
# MODULE 2.3a: Standard Library — os, sys, datetime, json
# =============================================================
# Python ships with a large standard library — "batteries included".
# No install needed; just import and use.

import os
import sys

print("=" * 55)
print("MODULE 2.3a: Standard Library — os, sys, datetime, json")
print("=" * 55)


# =============================================================
# os — interact with the operating system
# =============================================================
print("\n--- os module ---")

print(f"Current Working directory : {os.getcwd()}")
print(f"data/ exists?     : {os.path.exists('data')}")
print(f"Is a directory?   : {os.path.isdir('data')}")
print(f"Join path         : {os.path.join('data', 'students.csv')}")

if os.path.exists("data"):
    print(f"Files in data/    : {os.listdir('data')}")

# Create nested directories safely (exist_ok avoids error if already exists)
os.makedirs("data/output", exist_ok=True)
print("Ensured data/output/ exists")


# =============================================================
# sys — interpreter info and command-line arguments
# =============================================================
print("\n--- sys module ---")

print(f"Python version : {sys.version.split()[0]}")
print(f"Platform       : {sys.platform}")
# sys.argv holds CLI arguments: python script.py arg1 arg2
sys.argv = ["script.py", "arg1", "arg2"]
print(f"Script name    : {sys.argv[0]}")
