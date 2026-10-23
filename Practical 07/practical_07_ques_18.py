# Practical 7 - Question 18: NumPy basic indexing

# I use NumPy row and column indices to get the required elements.

# The coordinates [1, 2] in this exercise are zero-based indices.

# I import NumPy because this question uses arrays.
import numpy as np

# I keep the same elements and arrange them into the required shape.
array = np.arange(1, 10).reshape(3, 3)

# I display the result clearly.
print('Element [1, 2]:', array[1, 2])
print('Row:', array[1, :])
print('Column:', array[:, 2])
