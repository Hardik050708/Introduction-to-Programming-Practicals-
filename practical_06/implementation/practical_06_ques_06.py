# Practical 6 - Question 6: NumPy array creation

# NumPy creates typed arrays; shape records the size of each axis.
import numpy as np
for array in (np.array([[1, 2], [3, 4]]), np.zeros((2, 3)), np.ones((3, 2))):
    print(array)
    print("Shape:", array.shape, "Data type:", array.dtype)
