# Practical 7 - Slicing Question 2: Row and column access

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Second row:", matrix[1])
# Each row stores one value from the requested column.
print("Third column:", [row[2] for row in matrix])
