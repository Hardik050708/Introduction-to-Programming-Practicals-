# Practical 5 - Question 1: Break at five

# I use break before printing 5, so the loop stops at that point.

# I repeat this step for each value in the sequence.
for n in range(1, 11):
    if n == 5:
        # I stop this loop as soon as the required condition is met.
        break
    print(n)
