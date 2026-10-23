# Practical 4 - Question 4: Factorial using for and while

# I find the factorial using both loops and compare the two answers.

# First, I take the required input from the user.
n = int(input('Nonnegative integer: '))

# I check the input before using it in the calculation.
if n < 0:
    print('Factorial is undefined for negative integers.')
else:
    # I start the factorial at 1 because multiplying by zero would spoil the answer.
    for_result = 1
    # I repeat this step for each value in the sequence.
    for i in range(1, n + 1):
        for_result *= i
    # I start the factorial at 1 because multiplying by zero would spoil the answer.
    while_result = 1
    i = 1
    # I repeat the steps until the stopping condition is reached.
    while i <= n:
        while_result *= i
        i += 1
    print('For factorial:', for_result)
    print('While factorial:', while_result)
