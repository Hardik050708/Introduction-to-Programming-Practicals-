# Practical 6 - Question 9: Array statistics

# I find the mean, median and population standard deviation of the data.

# I use the population standard deviation, so NumPy keeps ddof=0.

# I import NumPy because this question uses arrays.
import numpy as np

# I store the given values in a NumPy array.
values = np.array([10, 20, 30, 40, 50])

# I display the result clearly.
print('Mean:', np.mean(values))
print('Median:', np.median(values))
print(f'Population standard deviation: {np.std(values):.4f}')
