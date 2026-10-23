# Practical 6 - Question 5: Matrix transpose

rows = int(input("Rows: "))
cols = int(input("Columns: "))
if rows <= 0 or cols <= 0:
    raise ValueError("Matrix dimensions must be positive.")
matrix = []
for i in range(rows):
    row = list(map(float, input(f"Row {i + 1} ({cols} numbers): ").split()))
    if len(row) != cols:
        raise ValueError("Incorrect number of columns.")
    matrix.append(row)

# Transpose exchanges the row and column indices.
transpose = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
print("Original:", matrix)
print("Transpose:", transpose)
