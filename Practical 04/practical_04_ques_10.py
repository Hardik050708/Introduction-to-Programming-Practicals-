# Practical 4 - Question 10: Nested loop patterns

# I use the outer loop for rows and the inner loop for each pattern value.

# First, I take the required input from the user.
rows = int(input('Rows: '))

# I check this condition to decide which step should run.
if rows < 1:
    print('Rows must be positive.')
else:
    print('Star triangle:')
    # I go through the rows one by one.
    for i in range(1, rows + 1):
        # I go through the columns one by one.
        for j in range(i):
            print('*', end='')
        print()
    print('Reverse star triangle:')
    for i in range(rows, 0, -1):
        for j in range(i):
            print('*', end='')
        print()
    print('Number triangle:')
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
    print('Reverse number triangle:')
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
