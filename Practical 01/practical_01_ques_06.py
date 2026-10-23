# Practical 1 - Question 6: Implicit and explicit conversion

# I compare automatic numeric conversion with conversion done using int() and str().

# I display the result clearly.
print('Implicit:', 5 + 2.5, type(5 + 2.5))

# I use try-except so the expected error does not stop the example.
try:
    print(5 + '2')
except TypeError:
    print('TypeError: int + string needs an explicit conversion.')

# I add the values and store the answer in numeric_addition.
numeric_addition = 5 + int('2')

# I display the result clearly.
print('Numeric addition:', numeric_addition)

# I add the values and store the answer in string_joining.
string_joining = str(5) + '2'

# I display the result clearly.
print('String joining:', string_joining)
