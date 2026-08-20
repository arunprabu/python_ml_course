# =============================================================
# MODULE 2.3c: CSV File Handling
# =============================================================
# CSV (Comma-Separated Values) is the most common flat-file format.
# Python's built-in 'csv' module handles reading and writing.

import csv
import os

print("=" * 55)
print("MODULE 2.3c: CSV File Handling")
print("=" * 55)

os.makedirs("data/output", exist_ok=True)


# =============================================================
# Reading CSV — csv.DictReader (each row becomes a dict)
# =============================================================
print("\n--- Reading CSV with DictReader ---")

csv_path = "data/students.csv"
students = []

with open(csv_path, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append(row)

print(f"Loaded {len(students)} students")
print(f"Columns : {list(students[0].keys())}")
print(f"\nFirst student:")
for key, val in students[0].items():
    print(f"  {key:<20} : {val}")


# =============================================================
# Processing the data
# =============================================================
print("\n--- Computing Averages ---")

mark_cols = ["marks_math", "marks_python", "marks_dbms", "marks_networks"]

print(f"\n{'Name':<22} {'Avg':>6}  Status")
print("-" * 38)
for s in students:
    marks = [int(s[col]) for col in mark_cols]
    avg = sum(marks) / len(marks)
    status = "PASS" if avg >= 60 else "FAIL"
    print(f"{s['name']:<22} {avg:>6.1f}  {status}")


# =============================================================
# Writing CSV — csv.DictWriter
# =============================================================
print("\n--- Writing CSV with DictWriter ---")

output_csv = "data/output/results.csv"
fieldnames = ["student_id", "name", "average", "status"]

with open(output_csv, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # writes the column names as the first row
    for s in students:
        marks = [int(s[col]) for col in mark_cols]
        avg = sum(marks) / len(marks)
        writer.writerow(
            {
                "student_id": s["student_id"],
                "name": s["name"],
                "average": round(avg, 2),
                "status": "PASS" if avg >= 60 else "FAIL",
            }
        )

print(f"Written to {output_csv}")

# Verify by reading back
print("\n--- Reading the written file back ---")
with open(output_csv, newline="") as f:
    for row in csv.DictReader(f):
        print(
            f"  {row['student_id']}  {row['name']:<22} {row['average']:>6}  {row['status']}"
        )


# =============================================================
# Writing CSV from a list of lists (csv.writer)
# =============================================================
print("\n--- csv.writer (plain rows, no dict) ---")

simple_csv = "data/output/simple.csv"
rows = [
    ["Name", "Score", "Grade"],
    ["Alice", 92, "A"],
    ["Bob", 74, "B"],
    ["Charlie", 58, "C"],
]

with open(simple_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)  # write all rows at once

print(f"Written {len(rows)} rows to {simple_csv}")
