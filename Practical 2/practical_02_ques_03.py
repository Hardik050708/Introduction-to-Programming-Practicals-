# Practical 2 - Question 3: Evaluate expressions

# I calculate the sum, average and given expression as separate steps.

# I start with an empty entered numbers list.
entered_numbers = []

# I convert each separated input into a number before storing it.
for number_text in input('Three numbers separated by spaces: ').split():
    entered_numbers.append(float(number_text))
a, b, c = entered_numbers

# I add the values and store the answer in total.
total = a + b + c

# I display the result clearly.
print('Sum:', total)

# I divide the values and store the answer in average.
average = (a + b + c) / 3

# I display the result clearly.
print('Average:', average)

# I divide the values and store the answer in expression_result.
expression_result = (a + b) * c / 2

# I display the result clearly.
print('(a + b) * c / 2:', expression_result)
