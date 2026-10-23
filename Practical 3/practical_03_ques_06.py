# Practical 3 - Question 6: Leap year

# I check the century rule as well as the divisibility-by-4 rule.

# First, I take the required input from the user.
year = int(input('Year: '))

# I check this condition to decide which step should run.
if year <= 0:
    print('Enter a positive year.')
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('Leap year')
else:
    print('Not a leap year')
