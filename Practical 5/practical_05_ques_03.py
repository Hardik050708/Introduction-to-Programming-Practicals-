# Practical 5 - Question 3: Compare break and continue

# I use the same condition in both loops to compare break and continue.

# I display the result clearly.
print('break:')

# I repeat this step for each value in the sequence.
for n in range(1, 11):
    if n == 5:
        # I stop this loop as soon as the required condition is met.
        break
    print(n, end=' ')

# I display the result clearly.
print('\ncontinue:')

# I repeat this step for each value in the sequence.
for n in range(1, 11):
    if n == 5:
        # I skip this value and continue with the next one.
        continue
    print(n, end=' ')

# I display the result clearly.
print()
