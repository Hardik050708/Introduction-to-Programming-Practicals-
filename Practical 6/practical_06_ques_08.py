# Practical 6 - Question 8: Array arithmetic

# I compare NumPy arithmetic with the steps needed for normal lists.

# I import NumPy because this question uses arrays.
import numpy as np

# I store the given values in a NumPy array.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# I add the values and store the answer in addition.
addition = a + b

# I display the result clearly.
print('Addition:', addition)

# I subtract the values and store the answer in subtraction.
subtraction = a - b

# I display the result clearly.
print('Subtraction:', subtraction)

# I multiply the values and store the answer in elementwise_multiplication.
elementwise_multiplication = a * b

# I display the result clearly.
print('Elementwise multiplication:', elementwise_multiplication)
x = [1, 2, 3]
y = [4, 5, 6]

# I add the values and store the answer in list_addition_concatenates.
list_addition_concatenates = x + y

# I display the result clearly.
print('List addition concatenates:', list_addition_concatenates)

# I start with an empty list sum list.
list_sum = []

# I repeat this step for each value in the sequence.
for i in range(len(x)):
    list_sum.append(x[i] + y[i])

# I display the result clearly.
print('List numeric addition:', list_sum)

# I start with an empty list difference list.
list_difference = []

# I repeat this step for each value in the sequence.
for i in range(len(x)):
    list_difference.append(x[i] - y[i])

# I display the result clearly.
print('List subtraction:', list_difference)

# I start with an empty list product list.
list_product = []

# I repeat this step for each value in the sequence.
for i in range(len(x)):
    list_product.append(x[i] * y[i])

# I display the result clearly.
print('List multiplication:', list_product)
