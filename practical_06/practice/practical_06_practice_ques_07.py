# Practical 6 - Practice Question 7: Heart rate reshape

# Sixty readings fit 12 rows with 5 readings per row.
import numpy as np
rates = np.array([72,74,73,75,76,74,73,72,78,80,82,79,77,76,75,74,73,72,71,70,
                  69,68,67,66,72,74,76,78,80,82,84,83,81,79,77,75,74,73,72,71,
                  70,69,68,67,66,65,72,74,76,78,80,82,84,86,88,85,83,81,79,77])
matrix = rates.reshape(12, 5)
print("Shape:", matrix.shape)
print(matrix)
