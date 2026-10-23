# Practical 8 - Question 6: Dictionary iteration

# I visit the keys, values and key-value pairs in separate loops.

student = {'name': 'Asha', 'age': 18, 'marks': 92}

# I display the result clearly.
print('Keys:')

# I repeat this step for each value in the sequence.
for key in student:
    print(key)

# I display the result clearly.
print('Values:')

# I repeat this step for each value in the sequence.
for value in student.values():
    print(value)

# I display the result clearly.
print('Pairs:')

# I repeat this step for each value in the sequence.
for key, value in student.items():
    print(key, value)
