# Practical 6 - Question 11: Matrix operations

import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
product = a @ b  # @ is matrix multiplication; * is elementwise multiplication.
manual = [[sum(int(a[i, k]) * int(b[k, j]) for k in range(2)) for j in range(2)] for i in range(2)]
print("Matrix product:\n", product)
print("Manual product:", manual)
print("Transpose:\n", a.T)
print("Manual transpose:", [[int(a[i, j]) for i in range(2)] for j in range(2)])
print("Products match:", np.array_equal(product, manual))
