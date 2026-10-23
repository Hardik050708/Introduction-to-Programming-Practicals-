# Practical 6 - Question 8: Array arithmetic

# NumPy arithmetic is elementwise, while list + concatenates the lists.
import numpy as np
a, b = np.array([1, 2, 3]), np.array([4, 5, 6])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Elementwise multiplication:", a * b)
x, y = [1, 2, 3], [4, 5, 6]
print("List addition concatenates:", x + y)
print("List numeric addition:", [x[i] + y[i] for i in range(len(x))])
print("List subtraction:", [x[i] - y[i] for i in range(len(x))])
print("List multiplication:", [x[i] * y[i] for i in range(len(x))])
