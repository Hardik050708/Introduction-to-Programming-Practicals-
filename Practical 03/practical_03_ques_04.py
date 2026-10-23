# Practical 3 - Question 4: Nested voting conditions

# I use nested if statements to check age and nationality separately.

# First, I take the required input from the user.
age = int(input('Age: '))
nationality = input('Nationality: ').strip().lower()

# I check this condition to decide which step should run.
if age >= 18:
    if nationality == 'indian':
        print('Eligible to vote')
    else:
        print('Not eligible: nationality must be Indian.')
else:
    print('Not eligible: age must be at least 18.')
