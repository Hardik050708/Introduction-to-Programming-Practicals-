# Practical 9 - Question 3: Return a square

# I return the square so I can use it in another calculation.

# This function returns the square instead of only printing it.
def square(number):
    # I return the result so it can be used by the calling code.
    return number * number

# First, I take the required input from the user.
number = float(input('Number: '))
result = square(number)

# I display the result clearly.
print('Square:', result)

# I add the values and store the answer in square_plus_one.
square_plus_one = result + 1

# I display the result clearly.
print('Square plus one:', square_plus_one)
