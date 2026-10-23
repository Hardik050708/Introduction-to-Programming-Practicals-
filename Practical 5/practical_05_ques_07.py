# Practical 5 - Question 7: Sum valid inputs

# I use zero to stop input and ignore negative numbers while adding.

# I start total at zero before counting or adding anything.
total = 0

# I repeat the steps until the stopping condition is reached.
while True:
    # I take the input needed in this step.
    n = float(input('Number (0 to stop): '))
    if n == 0:
        # I stop this loop as soon as the required condition is met.
        break
    # I check the input before using it in the calculation.
    if n < 0:
        # I skip this value and continue with the next one.
        continue
    total += n

# I display the result clearly.
print('Sum:', total)
