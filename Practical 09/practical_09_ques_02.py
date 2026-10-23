# Practical 9 - Question 2: Function parameters

# I pass the two input values to a function that returns their sum.

# This function takes two numbers and returns their sum.
def add(a, b):
    # I return the result so it can be used by the calling code.
    return a + b

# First, I take the required input from the user.
x = float(input('First number: '))
y = float(input('Second number: '))

# I display the result clearly.
print('Sum:', add(x, y))
