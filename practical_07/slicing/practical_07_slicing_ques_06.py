# Practical 7 - Slicing Question 6: NumPy basic indexing

import numpy as np
array = np.arange(1, 10).reshape(3, 3)
print("Element [1, 2]:", array[1, 2])  # Coordinates here are 0-based indices.
print("Row:", array[1, :])
print("Column:", array[:, 2])
