# Practical 8 - Question 9: Nested dictionaries

# I use the student ID first and then the detail key inside it.

students = {'S101': {'name': 'Asha', 'marks': 92}, 'S102': {'name': 'Ravi', 'marks': 85}}

# I display the result clearly.
print('S101 name:', students['S101']['name'])
students['S102']['marks'] = 90
print(students)
