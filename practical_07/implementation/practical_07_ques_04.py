# Practical 7 - Question 4: Mutability comparison

# Lists allow item assignment, but tuples reject it with TypeError.
numbers = [1, 2, 3]
fixed = (1, 2, 3)
numbers[0] = 10
print("Modified list:", numbers)
try:
    fixed[0] = 10
except TypeError:
    print("TypeError: tuple elements cannot be reassigned.")
