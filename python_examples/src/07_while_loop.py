# TODO: SELF-LEARN EXERCISE for TRAINEES
# =============================================================
# MODULE 1.3b: while Loop
# =============================================================
# Same as Java's while loop.
# Note: Python has NO -- operator. Use -= 1 instead.

print("=" * 55)
print("MODULE 1.3b: while Loop")
print("=" * 55)


# =============================================================
# Basic while loop
# =============================================================
print("\n--- countdown ---")

countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1  # no -- in Python
print("  Blast off!")


# # =============================================================
# # while with break — exit early when a condition is met
# # =============================================================
print("\n--- break: find first divisor ---")

n = 28
divisor = 2
while divisor <= n:
    if n % divisor == 0:
        print(f"  First divisor of {n} is {divisor}")
        break
    divisor += 1


# # =============================================================
# # while with continue — skip an iteration and keep going
# # =============================================================
print("\n--- continue: print odd numbers only ---")

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # skip even numbers, jump back to 'while'
    print(f"  {i}", end=" ")
print()


# # =============================================================
# # while-else — else block runs when the loop finishes normally
# # (i.e. NOT via break).  Java has no equivalent.
# # =============================================================
print("\n--- while-else ---")

target = 37
num = 2
while num < target:
    if target % num == 0:
        print(f"  {target} is NOT prime (divisible by {num})")
        break
    num += 1
else:
    # reached here only because the while condition became False
    print(f"  {target} IS prime")
