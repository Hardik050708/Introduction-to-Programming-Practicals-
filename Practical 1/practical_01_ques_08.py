# Practical 1 - Question 8: Swapping variables

# I try both the temporary-variable method and tuple unpacking for swapping.

a = 10
b = 20
temp = a
a = b
b = temp

# I display the result clearly.
print('Third variable:', a, b)
a = 10
b = 20
a, b = (b, a)
print('Tuple unpacking:', a, b)
