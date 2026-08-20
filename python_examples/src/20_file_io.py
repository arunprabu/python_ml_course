# =============================================================
# MODULE 2.3b: File I/O with the 'with' Statement
# =============================================================
# 'with' automatically closes the file — even if an error occurs.
# Java equivalent: try-with-resources  (try (FileWriter f = ...) { })

import os
from pathlib import Path

print("=" * 55)
print("MODULE 2.3b: File I/O with the 'with' Statement")
print("=" * 55)


os.makedirs("data/output", exist_ok=True)
sample_file = "data/output/notes.txt"

# # =============================================================
# # Writing a file — mode "w" (creates or overwrites)
# # =============================================================
print("\n--- Write (mode='w') ---")

with open(sample_file, "w") as f:
    print("======About to write into file.....====")
    f.write("Line 1: Python is fun!\n")
    f.write("Line 2: File I/O is easy.\n")
    f.write("Line 3: 'with' ensures the file is closed.\n")

print(f"Written to {sample_file}")


# # =============================================================
# # Appending — mode "a" (adds to end, does NOT overwrite)
# # =============================================================
print("\n--- Append (mode='a') ---")

with open(sample_file, "a") as f:
    f.write("Line 4: Appended later.\n")
print("Appended one more line")


# =============================================================
# Reading the entire file at once
# =============================================================
# print("\n--- Read entire file ---")

# with open(sample_file, "r") as f:  # "r" is the default mode
#     content = f.read()
# print(content)


# =============================================================
# Reading line by line (efficient for large files)
# =============================================================
print("--- Read line by line ---")

with open(sample_file, "r") as f:
    for start_no, line in enumerate(f, start=10):
        if start_no <= 10:
            print(
                f"  Starting at {start_no}: {line.rstrip()}"
            )  # rstrip removes trailing \n

# =============================================================
# Reading into a list
# =============================================================
print("\n--- readlines() → list ---")

with open(sample_file, "r") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
print(f"First line : {lines[0].rstrip()}")
print(f"Last line  : {lines[-1].rstrip()}")


# =============================================================
# pathlib — modern, cross-platform path handling
# Cleaner than concatenating strings like "data/" + "file.txt"
# =============================================================
print("\n--- pathlib (modern path handling) ---")

path = Path("data/output/notes2.txt")
print(f"Full path  : {path}")
print(f"File name  : {path.name}")
print(f"Extension  : {path.suffix}")
print(f"Stem       : {path.stem}")  # name without extension
print(f"Parent dir : {path.parent}")
print(f"Exists?    : {path.exists()}")
print(f"Is file?   : {path.is_file()}")

# # pathlib can also read/write directly
text = path.read_text()
print(f"\nRead via pathlib ({len(text.splitlines())} lines)")
