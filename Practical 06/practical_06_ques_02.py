# Practical 6 - Question 2: Matrix traversal

# I change the order of the loops to visit the matrix row-wise and column-wise.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# I display the result clearly.
print('Row-wise:')

# I go through the rows one by one.
for row in matrix:
    # I repeat this step for each value in the sequence.
    for value in row:
        print(value, end=' ')
    print()

# I display the result clearly.
print('Column-wise:')

# I repeat this step for each value in the sequence.
for col in range(3):
    # I go through the rows one by one.
    for row in range(3):
        print(matrix[row][col], end=' ')
    print()
