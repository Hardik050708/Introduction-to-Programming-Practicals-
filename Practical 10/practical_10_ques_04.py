# Practical 10 - Question 4: String immutability

# I show that strings cannot be edited in place and make a new string instead.

text = 'python'

# I use try-except so the expected error does not stop the example.
try:
    text[0] = 'P'
except TypeError:
    print('TypeError: strings cannot be changed in place.')

# I add the values and store the answer in text.
text = 'P' + text[1:]

# I display the result clearly.
print('Corrected:', text)
