# Practical 7 - Question 15: Negative 2D indices

# Negative indices select from the end of each dimension.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Last row:", matrix[-1], matrix[2])
print("Last column:", [row[-1] for row in matrix], [row[2] for row in matrix])
print("Bottom-right:", matrix[-1][-1], matrix[2][2])
