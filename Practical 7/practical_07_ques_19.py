# Practical 7 - Question 19: NumPy row and column slices

# I compare NumPy slicing with the loop needed for a list column.

# I import NumPy because this question uses arrays.
import numpy as np

# I keep the same elements and arrange them into the required shape.
array = np.arange(1, 10).reshape(3, 3)

# I display the result clearly.
print('First two rows:\n', array[:2, :])
print('Last column:', array[:, -1])
matrix = array.tolist()
print('List rows:', matrix[:2])

# I start with an empty last column list.
last_column = []

# I go through the rows one by one.
for row in matrix:
    last_column.append(row[-1])

# I display the result clearly.
print('List column:', last_column)
