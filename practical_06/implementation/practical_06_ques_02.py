# Practical 6 - Question 2: Matrix traversal

# Swap the loop order to traverse by columns instead of rows.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Row-wise:")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
print("Column-wise:")
for col in range(3):
    for row in range(3):
        print(matrix[row][col], end=" ")
    print()
