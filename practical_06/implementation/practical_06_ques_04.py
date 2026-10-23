# Practical 6 - Question 4: Matrix addition

# Add corresponding cells using matching row and column indices.
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

second = []
print("Second matrix:")
for i in range(rows):
    row = list(map(float, input(f"Row {i + 1} ({cols} numbers): ").split()))
    if len(row) != cols:
        raise ValueError("Incorrect number of columns.")
    second.append(row)
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix[i][j] + second[i][j])
    result.append(row)
print("Sum:")
for row in result:
    print(row)
