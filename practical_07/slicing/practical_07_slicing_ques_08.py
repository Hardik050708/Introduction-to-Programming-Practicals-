# Practical 7 - Slicing Question 8: NumPy middle submatrix

import numpy as np
array = np.arange(1, 17).reshape(4, 4)
# NumPy slices both dimensions together; nested lists need row-by-row slicing.
print("Middle 2x2:\n", array[1:3, 1:3])
