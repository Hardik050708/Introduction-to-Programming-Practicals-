# Practical 1 - Question 9: Data type based calculator

# I add two numeric values or join two strings after checking their types.

from ast import literal_eval

# I try to identify the entered value before choosing the operation.
def detect(text):
    # I use try-except so the expected error does not stop the example.
    try:
        return literal_eval(text)
    except (ValueError, SyntaxError):
        return text

# First, I take the required input from the user.
a = detect(input('First value (number or text): '))
b = detect(input('Second value (number or text): '))

# I display the result clearly.
print('Types:', type(a).__name__, type(b).__name__)

# I check this condition to decide which step should run.
if type(a) in (int, float) and type(b) in (int, float):
    # I add the values and store the answer in addition_result.
    addition_result = a + b
    print('Sum:', addition_result)
elif isinstance(a, str) and isinstance(b, str):
    # I add the values and store the answer in concatenation.
    concatenation = a + b
    print('Concatenation:', concatenation)
else:
    print('Invalid combination: enter two numbers or two strings.')
