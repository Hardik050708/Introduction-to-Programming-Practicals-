# Practical 8 - Question 11: Sort dictionary data

# I arrange dictionary entries once by key and once by value.

marks = {'Ravi': 85, 'Asha': 92, 'Neha': 78}

# I display the result clearly.
print('By keys:', dict(sorted(marks.items())))
print('By values:', dict(sorted(marks.items(), key=lambda item: item[1])))
