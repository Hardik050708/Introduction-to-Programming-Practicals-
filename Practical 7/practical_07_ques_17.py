# Practical 7 - Question 17: List submatrix

# I slice each selected row to build the top-left submatrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# I start with an empty sub list.
sub = []

# I go through the rows one by one.
for row in matrix[:2]:
    sub.append(row[:2])

# I display the result clearly.
print(sub)
