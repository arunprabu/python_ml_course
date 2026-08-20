# list in python
# the following is for type hint -- not enforced by python
# from typing import List

# list - group of similar items
colors = ["red", "green", "blue"]
print(colors[0])
print(colors[1])
print(colors[2])

print(f"Length of the List: {len(colors)}")  # length of the list

subjects = ["Math", "English", "Science", "History"]
subjects[0] = "Mathematics"  # changing the first item

# let's loop thru the list
for subject in subjects:
    print(subject)
