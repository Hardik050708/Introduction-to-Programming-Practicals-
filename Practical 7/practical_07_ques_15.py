# Practical 7 - Question 15: Negative 2D indices

# I compare negative indices with their positive-index equivalents.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# I display the result clearly.
print('Last row:', matrix[-1], matrix[2])

# I start with an empty negative index column list.
negative_index_column = []

# I go through the rows one by one.
for row in matrix:
    negative_index_column.append(row[-1])

# I start with an empty positive index column list.
positive_index_column = []

# I go through the rows one by one.
for row in matrix:
    positive_index_column.append(row[2])

# I display the result clearly.
print('Last column:', negative_index_column, positive_index_column)
print('Bottom-right:', matrix[-1][-1], matrix[2][2])
