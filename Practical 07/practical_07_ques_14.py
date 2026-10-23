# Practical 7 - Question 14: Row and column access

# I take the second row directly and collect the third column using a loop.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# I display the result clearly.
print('Second row:', matrix[1])

# I start with an empty third column list.
third_column = []

# I go through the rows one by one.
for row in matrix:
    third_column.append(row[2])

# I display the result clearly.
print('Third column:', third_column)
