# Practical 2 - Question 8: Multiple inputs in one line

# I separate the three inputs before finding their sum and product.

# I start with an empty entered numbers list.
entered_numbers = []

# I convert each separated input into a number before storing it.
for number_text in input('Enter three numbers: ').split():
    entered_numbers.append(float(number_text))
a, b, c = entered_numbers

# I display the result clearly.
print(f'Sum: {a + b + c:g}')
print(f'Product: {a * b * c:g}')
