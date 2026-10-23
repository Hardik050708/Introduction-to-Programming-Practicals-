# Practical 7 - Question 18: NumPy basic indexing

import numpy as np
array = np.arange(1, 10).reshape(3, 3)
print("Element [1, 2]:", array[1, 2])  # Coordinates here are 0-based indices.
print("Row:", array[1, :])
print("Column:", array[:, 2])
