# Practical 7 - Question 19: NumPy row and column slices

# NumPy slices both axes together; list column access visits each row.
import numpy as np
array = np.arange(1, 10).reshape(3, 3)
print("First two rows:\n", array[:2, :])
print("Last column:", array[:, -1])
matrix = array.tolist()
print("List rows:", matrix[:2])
print("List column:", [row[-1] for row in matrix])
