# Practical 4 - Question 9: Fibonacci iteration

# I keep two consecutive terms and calculate the next Fibonacci term.

# First, I take the required input from the user.
n = int(input('Number of terms: '))

# I check the input before using it in the calculation.
if n < 0:
    print('Count cannot be negative.')
else:
    a = 0
    b = 1
    # I repeat this step for each value in the sequence.
    for i in range(n):
        print(a, end=' ')
        # I find the next term before changing the previous two terms.
        next_term = a + b
        a = b
        b = next_term
    print()
