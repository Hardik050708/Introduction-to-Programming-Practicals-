# Practical 5 - Question 10: Pattern with skipped even values

# I use continue inside the inner loop to skip even pattern values.

# First, I take the required input from the user.
rows = int(input('Rows: '))

# I go through the rows one by one.
for row in range(1, rows + 1):
    # I repeat this step for each value in the sequence.
    for value in range(1, row + 1):
        if value % 2 == 0:
            # I skip this value and continue with the next one.
            continue
        print(value, end=' ')
    print()
