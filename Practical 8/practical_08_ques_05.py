# Practical 8 - Question 5: Remove dictionary entries

# I remove entries with pop() and del and check a missing key.

student = {'name': 'Asha', 'age': 18, 'marks': 92}

# I display the result clearly.
print('Removed marks:', student.pop('marks'))
del student['age']
print('Remaining:', student)

# I use try-except so the expected error does not stop the example.
try:
    del student['city']
except KeyError:
    print('KeyError: city is absent.')

# I display the result clearly.
print('Safe missing pop:', student.pop('city', 'Not found'))
