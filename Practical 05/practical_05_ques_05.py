# Practical 5 - Question 5: First divisible number

# I check numbers from 1 to 100 and stop at the first divisible number.

# First, I take the required input from the user.
n = int(input('Divisor: '))

# I check this condition to decide which step should run.
if n == 0:
    print('Divisor cannot be zero.')
else:
    # I repeat this step for each value in the sequence.
    for number in range(1, 101):
        # I use the remainder to check this condition.
        if number % n == 0:
            print('First divisible number:', number)
            # I stop this loop as soon as the required condition is met.
            break
    else:
        print('No divisible number between 1 and 100.')
