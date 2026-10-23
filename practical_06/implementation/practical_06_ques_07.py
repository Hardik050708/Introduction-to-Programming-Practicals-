# Practical 6 - Question 7: NumPy indexing and slicing

# Use separate row and column selectors to access or slice a 2D NumPy array.
import numpy as np
array = np.arange(1, 10).reshape(3, 3)
print("Element [1, 2]:", array[1, 2])
print("Row 2:", array[1, :])
print("Column 3:", array[:, 2])
print("Top-left 2x2:\n", array[:2, :2])
