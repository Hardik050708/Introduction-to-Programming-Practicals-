# Practical 6 - Question 7: NumPy indexing and slicing

# I use separate row and column indices to access and slice the array.

# I import NumPy because this question uses arrays.
import numpy as np

# I keep the same elements and arrange them into the required shape.
array = np.arange(1, 10).reshape(3, 3)

# I display the result clearly.
print('Element [1, 2]:', array[1, 2])
print('Row 2:', array[1, :])
print('Column 3:', array[:, 2])
print('Top-left 2x2:\n', array[:2, :2])
