# Practical 7 - Question 8: Tuple methods

# I count repeated values and find the first index of a selected value.

values = (10, 20, 10, 30)

# I display the result clearly.
print('Count of 10:', values.count(10))
print('Index of 20:', values.index(20))

# I use try-except so the expected error does not stop the example.
try:
    print(values.index(99))
except ValueError:
    print('ValueError: 99 is not in the tuple.')
