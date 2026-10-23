# Practical 3 - Question 7: Conditional calculator

# I select the operation using if-elif and check the divisor before dividing.

# First, I take the required input from the user.
a = float(input('First number: '))
b = float(input('Second number: '))
op = input('Operator (+, -, *, /): ').strip()

# I check this condition to decide which step should run.
if op == '+':
    # I add the values and store the answer in result.
    result = a + b
    print('Result:', result)
elif op == '-':
    # I subtract the values and store the answer in difference.
    difference = a - b
    print('Result:', difference)
elif op == '*':
    # I multiply the matching row and column values.
    product = a * b
    print('Result:', product)
elif op == '/':
    # I check that the divisor is not zero before dividing.
    if b != 0:
        # I divide the values and store the answer in division_result.
        division_result = a / b
    else:
        division_result = 'Cannot divide by zero'
    print('Result:', division_result)
else:
    print('Invalid operator')
