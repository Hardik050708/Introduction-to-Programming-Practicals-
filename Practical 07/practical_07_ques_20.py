# Practical 7 - Question 20: NumPy middle submatrix

# I use row and column slices together to extract the middle 2 by 2 section.

# I import NumPy because this question uses arrays.
import numpy as np

# I keep the same elements and arrange them into the required shape.
array = np.arange(1, 17).reshape(4, 4)

# I display the result clearly.
print('Middle 2x2:\n', array[1:3, 1:3])
