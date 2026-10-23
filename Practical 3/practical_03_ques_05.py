# Practical 3 - Question 5: Largest of three

# I compare all three numbers and use >= so equal values are handled.

# I start with an empty entered numbers list.
entered_numbers = []

# I convert each separated input into a number before storing it.
for number_text in input('Three numbers: ').split():
    entered_numbers.append(float(number_text))
a, b, c = entered_numbers

# I check this condition to decide which step should run.
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# I display the result clearly.
print('Largest:', largest)
