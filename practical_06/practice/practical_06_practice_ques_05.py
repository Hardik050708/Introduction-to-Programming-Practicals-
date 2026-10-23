# Practical 6 - Practice Question 5: Warehouse stock

# Use axis sums for shelf/bin totals and argwhere for maximum-bin coordinates.
import numpy as np
stock = np.array([[10,12,15,18,20,16,14,13,11,9], [8,10,12,14,16,18,20,22,24,26],
                  [5,7,9,11,13,15,17,19,21,23], [30,28,26,24,22,20,18,16,14,12]])
row_totals = stock.sum(axis=1)
print("Busiest shelf:", int(row_totals.argmax()) + 1)
print("Maximum stocked bin(s) [shelf, bin]:", np.argwhere(stock == stock.max()) + 1)
print("Maximum quantity:", stock.max())
print("Row totals:", row_totals)
print("Column totals:", stock.sum(axis=0))
