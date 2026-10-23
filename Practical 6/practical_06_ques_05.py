# Practical 6 - Question 5: Matrix transpose

# I make the transpose by turning each original column into a new row.

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

# I start with an empty transpose list.
transpose = []

# I go through the columns one by one.
for column_number in range(cols):
    # I start with an empty new row list.
    new_row = []
    # I go through the rows one by one.
    for row_number in range(rows):
        value = matrix[row_number][column_number]
        new_row.append(value)
    transpose.append(new_row)

# I display the result clearly.
print('Original:', matrix)
print('Transpose:', transpose)
