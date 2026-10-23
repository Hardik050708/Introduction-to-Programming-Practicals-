# Practical 7 - Question 4: Mutability comparison

# I change a list value and check why the same change fails for a tuple.

numbers = [1, 2, 3]
fixed = (1, 2, 3)
numbers[0] = 10

# I display the result clearly.
print('Modified list:', numbers)

# I use try-except so the expected error does not stop the example.
try:
    fixed[0] = 10
except TypeError:
    print('TypeError: tuple elements cannot be reassigned.')
