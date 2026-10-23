# Practical 6 - Question 3: Row and column sums

# I add the values in each row and then in each column.

# First, I take the required input from the user.
rows = int(input('Rows: '))
cols = int(input('Columns: '))

# I check the input before using it in the calculation.
if rows <= 0 or cols <= 0:
    raise ValueError('Matrix dimensions must be positive.')

# I start with an empty matrix list.
matrix = []

# I go through the rows one by one.
for i in range(rows):
    # I start with an empty row list.
    row = []
    # I convert each separated input into a number before storing it.
    for number_text in input(f'Row {i + 1} ({cols} numbers): ').split():
        row.append(float(number_text))
    if len(row) != cols:
        raise ValueError('Incorrect number of columns.')
    matrix.append(row)
for i in range(rows):
    print(f'Row {i + 1} sum:', sum(matrix[i]))

# I go through the columns one by one.
for j in range(cols):
    # I start total at zero before counting or adding anything.
    total = 0
    # I go through the rows one by one.
    for i in range(rows):
        total += matrix[i][j]
    print(f'Column {j + 1} sum:', total)
