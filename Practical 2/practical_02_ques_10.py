# Practical 2 - Question 10: Error analysis

# I catch the example errors and show how to avoid them.

# I use try-except so the expected error does not stop the example.
try:
    print(10 / 0)
except ZeroDivisionError:
    print('ZeroDivisionError: the divisor cannot be zero.')
try:
    print('10' + 5)
except TypeError:
    print('TypeError: convert strings before numeric addition.')
divisor = 0

# I check this condition to decide which step should run.
if divisor != 0:
    print(10 / divisor)
else:
    print('Division prevented: divisor is zero.')

# I add the values and store the answer in correct_addition.
correct_addition = int('10') + 5

# I display the result clearly.
print('Correct addition:', correct_addition)
