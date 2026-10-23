# Practical 1 - Question 10: Boolean logic

# I store the comparisons as Boolean values before making the decision.

# First, I take the required input from the user.
age = int(input('Age: '))
marks = float(input('Marks: '))
is_adult = age > 18
has_passed = marks > 50

# I display the result clearly.
print('Age > 18:', is_adult)
print('Marks > 50:', has_passed)

# I check this condition to decide which step should run.
if is_adult and has_passed:
    print('Both conditions are satisfied.')
else:
    print('At least one condition is false.')
