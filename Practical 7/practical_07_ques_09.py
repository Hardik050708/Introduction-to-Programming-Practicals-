# Practical 7 - Question 9: Nested lists

# I access the inner list before changing its middle value.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# I display the result clearly.
print('Middle element:', matrix[1][1])
matrix[1][1] = 50
print('Updated matrix:', matrix)
