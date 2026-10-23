# Practical 6 - Question 10: Reshaping arrays

# I try valid shapes and catch the error when the element counts do not match.

# I import NumPy because this question uses arrays.
import numpy as np
values = np.arange(1, 13)

# I display the result clearly.
print('1D:', values)
print('3x4:\n', values.reshape(3, 4))
print('2x6:\n', values.reshape(2, 6))

# I use try-except so the expected error does not stop the example.
try:
    print(values.reshape(5, 3))
except ValueError:
    print('Cannot reshape: the number of elements must stay 12.')
