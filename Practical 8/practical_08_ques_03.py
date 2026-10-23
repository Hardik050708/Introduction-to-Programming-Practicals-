# Practical 8 - Question 3: Safe get method

# I use get() to supply a default when a key is missing.

student = {'name': 'Asha', 'age': 18, 'marks': 92}

# I display the result clearly.
print('Name:', student.get('name'))
print('City:', student.get('city', 'Unknown'))
