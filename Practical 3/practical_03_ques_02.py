# Practical 3 - Question 2: Even or odd

# I check the remainder after dividing by 2 to decide even or odd.

# First, I take the required input from the user.
number = int(input('Integer: '))

# I use the remainder to check this condition.
if number % 2 == 0:
    print('Even')
else:
    print('Odd')
