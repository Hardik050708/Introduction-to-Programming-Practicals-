# Practical 6 - Question 3: Row and column sums

# Each row sum uses one row; each column sum visits that column in every row.
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

for i in range(rows):
    print(f"Row {i + 1} sum:", sum(matrix[i]))
for j in range(cols):
    total = 0
    for i in range(rows):
        total += matrix[i][j]
    print(f"Column {j + 1} sum:", total)
