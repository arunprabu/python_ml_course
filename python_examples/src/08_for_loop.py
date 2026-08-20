# =============================================================
# MODULE 1.3c: for Loop and range()
# =============================================================
# Python's for loop is like Java's for-each — it iterates over sequences.
# To get the classic  for(int i=0; i<n; i++)  behaviour, use range().

print("=" * 55)
print("MODULE 1.3c: for Loop and range()")
print("=" * 55)


# =============================================================
# range() — generates a sequence of numbers
# =============================================================
# range(stop)              → starts from 0 to stop-1
# range(start, stop)       → start to stop-1
# range(start, stop, step) → with a custom step

# If you have a list with 5 items, their indexes are 0, 1, 2, 3, 4.


print("\n--- range(5): 0 to 4 ---")
for i in range(5):
    print(f"  i = {i}")
print()


print("\n--- range(10, 20): 10 to 19 ---")
for i in range(10, 20):
    print(i)
print()


print("\n--- range(0, 20, 3): step of 3 ---")
for i in range(0, 20, 3):
    print(i, end=" ")
print()

print("\n--- range(10, 0, -2): count down by 2 ---")
for i in range(10, 0, -2):
    print(i, end=" ")
print()


# # =============================================================
# # Iterating over a list (like Java for-each)
# # =============================================================
# print("\n--- for over a list ---")

# subjects = ["Math", "English", "Science", "History"]
# for subject in subjects:
#     print(f"  Subject: {subject}")
