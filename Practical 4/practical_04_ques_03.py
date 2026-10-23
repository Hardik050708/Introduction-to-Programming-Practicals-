# Practical 4 - Question 3: Sum and average with a loop

# I keep adding each number to a running total and divide by the count.

# First, I take the required input from the user.
n = int(input('How many numbers? '))

# I check this condition to decide which step should run.
if n <= 0:
    print('Count must be positive.')
else:
    # I start total at zero before counting or adding anything.
    total = 0
    # I repeat this step for each value in the sequence.
    for i in range(n):
        total += float(input(f'Number {i + 1}: '))
    print('Sum:', total)
    # I divide the values and store the answer in average.
    average = total / n
    print('Average:', average)
