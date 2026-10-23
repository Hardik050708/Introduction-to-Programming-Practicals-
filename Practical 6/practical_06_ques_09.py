# Practical 6 - Question 9: Array statistics

import numpy as np
values = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(values))
print("Median:", np.median(values))
print(f"Population standard deviation: {np.std(values):.4f}")  # ddof=0 uses all values.
