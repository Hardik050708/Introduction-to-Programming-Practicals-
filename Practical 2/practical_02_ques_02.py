# Practical 2 - Question 2: Numeric input handling

# I convert the two inputs before doing the four arithmetic operations.

# First, I take the required input from the user.
x = input('First number: ')
y = input('Second number: ')

# I add the values and store the answer in without_conversion_concatenation.
without_conversion_concatenation = x + y

# I display the result clearly.
print('Without conversion (concatenation):', without_conversion_concatenation)
a = float(x)
b = float(y)

# I add the values and store the answer in addition.
addition = a + b

# I display the result clearly.
print('Addition:', addition)

# I subtract the values and store the answer in subtraction.
subtraction = a - b

# I display the result clearly.
print('Subtraction:', subtraction)

# I multiply the values and store the answer in multiplication.
multiplication = a * b

# I display the result clearly.
print('Multiplication:', multiplication)

# I check that the divisor is not zero before dividing.
if b != 0:
    # I divide the values and store the answer in division_result.
    division_result = a / b
else:
    division_result = 'Undefined: division by zero'

# I display the result clearly.
print('Division:', division_result)
