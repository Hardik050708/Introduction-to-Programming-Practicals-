# Practical 5 - Question 2: Skip multiples of three

# I use continue to leave out multiples of 3.

# I repeat this step for each value in the sequence.
for n in range(1, 11):
    # I use the remainder to check this condition.
    if n % 3 == 0:
        # I skip this value and continue with the next one.
        continue
    print(n, end=' ')

# I display the result clearly.
print()
