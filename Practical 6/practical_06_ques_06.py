# Practical 6 - Question 6: NumPy array creation

import numpy as np

# I create each array using the method asked in the manual.
number_array = np.array([[1, 2], [3, 4]])
zero_array = np.zeros((2, 3))
one_array = np.ones((3, 2))

# I display the values, shape and data type of each array.
print(number_array)
print("Shape:", number_array.shape, "Data type:", number_array.dtype)

print(zero_array)
print("Shape:", zero_array.shape, "Data type:", zero_array.dtype)

print(one_array)
print("Shape:", one_array.shape, "Data type:", one_array.dtype)
