# Practical 7 - Question 17: List submatrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# I use the slicing-and-loop expression shown in the manual.
sub = [row[0:2] for row in matrix[0:2]]
print(sub)

# A nested list needs a separate column slice for each selected row.
