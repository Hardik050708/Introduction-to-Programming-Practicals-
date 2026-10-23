# Practical 8 - Question 2: Dictionary indexing

# I access values by key and handle an example missing-key error.

student = {'name': 'Asha', 'age': 18, 'marks': 92}

# I display the result clearly.
print('Name:', student['name'])
print('Marks:', student['marks'])

# I use try-except so the expected error does not stop the example.
try:
    print(student['city'])
except KeyError:
    print('KeyError: city is not present.')
