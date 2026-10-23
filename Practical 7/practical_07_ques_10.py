# Practical 7 - Question 10: List and tuple conversion

# I convert between list and tuple so I can edit the data when needed.

numbers = [1, 2, 3]
fixed = tuple(numbers)

# I display the result clearly.
print('Tuple:', fixed)
editable = list(fixed)
editable[0] = 10
print('Modified list:', editable)
print('Original tuple:', fixed)
