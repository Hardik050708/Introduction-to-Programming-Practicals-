# Practical 10 - Question 6: Find and index

# I compare find() returning -1 with index() raising an error.

text = 'Python makes programming easy'

# I display the result clearly.
print('find programming:', text.find('programming'))
print('index programming:', text.index('programming'))
print('find missing:', text.find('Java'))

# I use try-except so the expected error does not stop the example.
try:
    print(text.index('Java'))
except ValueError:
    print('index missing: ValueError')
