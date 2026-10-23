# Practical 7 - Question 17: List submatrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Nested lists need a slice for each row; matrix[:2, :2] is invalid.
sub = [row[:2] for row in matrix[:2]]
print(sub)
