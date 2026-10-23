# Practical 6 - Question 6: NumPy array creation

# I create NumPy arrays in three ways and check their shape and data type.

# I import NumPy because this question uses arrays.
import numpy as np

# I repeat this step for each value in the sequence.
for array in (np.array([[1, 2], [3, 4]]), np.zeros((2, 3)), np.ones((3, 2))):
    print(array)
    print('Shape:', array.shape, 'Data type:', array.dtype)
