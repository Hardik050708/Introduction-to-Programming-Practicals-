# Practical 6 - Question 4: Matrix addition

# I add the two matrices by adding cells at matching positions.

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

# I start with an empty second list.
second = []

# I display the result clearly.
print('Second matrix:')

# I go through the rows one by one.
for i in range(rows):
    # I start with an empty row list.
    row = []
    # I convert each separated input into a number before storing it.
    for number_text in input(f'Row {i + 1} ({cols} numbers): ').split():
        row.append(float(number_text))
    if len(row) != cols:
        raise ValueError('Incorrect number of columns.')
    second.append(row)

# I start with an empty result list.
result = []

# I go through the rows one by one.
for i in range(rows):
    # I start with an empty row list.
    row = []
    # I go through the columns one by one.
    for j in range(cols):
        row.append(matrix[i][j] + second[i][j])
    result.append(row)

# I display the result clearly.
print('Sum:')

# I go through the rows one by one.
for row in result:
    print(row)
