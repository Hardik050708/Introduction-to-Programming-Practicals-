# Practical 7 - Question 9: Nested lists

# The first index selects a row and the second selects a value within it.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Middle element:", matrix[1][1])
matrix[1][1] = 50
print("Updated matrix:", matrix)
