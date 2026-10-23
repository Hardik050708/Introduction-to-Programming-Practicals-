# Practical 7 - Question 11: Iteration and summation

# I use a loop to display and add the items of both sequence types.

# I repeat this step for each value in the sequence.
for values in ([10, 20, 30], (10, 20, 30)):
    # I start total at zero before counting or adding anything.
    total = 0
    # I repeat this step for each value in the sequence.
    for value in values:
        print(value, end=' ')
        total += value
    print('\nSum:', total)
