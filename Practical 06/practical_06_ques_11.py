# Practical 6 - Question 11: Matrix operations

# I compare the NumPy matrix operations with my manual nested-loop calculation.

# Matrix multiplication adds products; it is different from elementwise multiplication.

# I import NumPy because this question uses arrays.
import numpy as np

# I store the given values in a NumPy array.
first_matrix = np.array([[1, 2], [3, 4]])
second_matrix = np.array([[5, 6], [7, 8]])
numpy_product = np.matmul(first_matrix, second_matrix)

# I start with an empty manual product list.
manual_product = []

# I go through the rows one by one.
for row_number in range(2):
    # I start with an empty new row list.
    new_row = []
    # I go through the columns one by one.
    for column_number in range(2):
        # I start total at zero before counting or adding anything.
        total = 0
        # I use this loop to calculate each part of the answer.
        for position in range(2):
            first_value = int(first_matrix[row_number][position])
            second_value = int(second_matrix[position][column_number])
            # I multiply the matching row and column values.
            product = first_value * second_value
            # I add the values and store the answer in total.
            total = total + product
        new_row.append(total)
    manual_product.append(new_row)
numpy_transpose = first_matrix.transpose()

# I start with an empty manual transpose list.
manual_transpose = []

# I go through the columns one by one.
for column_number in range(2):
    # I start with an empty new row list.
    new_row = []
    # I go through the rows one by one.
    for row_number in range(2):
        value = int(first_matrix[row_number][column_number])
        new_row.append(value)
    manual_transpose.append(new_row)

# I display the result clearly.
print('Matrix product:\n', numpy_product)
print('Manual product:', manual_product)
print('Transpose:\n', numpy_transpose)
print('Manual transpose:', manual_transpose)
answers_match = np.array_equal(numpy_product, manual_product)
print('Products match:', answers_match)
