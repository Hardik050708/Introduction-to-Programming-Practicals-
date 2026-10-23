# Practical 3 - Question 3: Grade with elif

# I check the grade cutoffs from highest to lowest.

# First, I take the required input from the user.
percentage = float(input('Marks (0-100): '))

# I check the highest grade cutoff first.
if not 0 <= percentage <= 100:
    print('Invalid marks.')
else:
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 75:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'Fail'
    print('Grade:', grade)
