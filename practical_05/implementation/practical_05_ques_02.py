# Practical 5 - Question 2: Skip multiples of three

for n in range(1, 11):
    if n % 3 == 0:
        continue  # Skip this iteration only.
    print(n, end=" ")
print()
