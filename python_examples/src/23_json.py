# =============================================================
# json — serialize Python objects to JSON and back
# =============================================================
import json

print("\n--- json module ---")

employee = {
    "id": "E001",
    "name": "Alice",
    "skills": ["Python", "Django", "SQL"],
    "salary": 75000,
    "active": True,
}


# dict → JSON string
json_string = json.dumps(employee, indent=2)
print("Serialized to JSON:")
print(json_string)

# JSON string → dict
parsed = json.loads(json_string)
print(f"\nParsed back → name: {parsed}")

# # Write to file
json_path = "data/output/employee.json"
with open(json_path, "w") as f:
    json.dump(employee, f, indent=2)
print(f"Written to {json_path}")

# # Read from file
with open(json_path, "r") as f:
    loaded = json.load(f)
print(f"Loaded from file → name: {loaded}")
