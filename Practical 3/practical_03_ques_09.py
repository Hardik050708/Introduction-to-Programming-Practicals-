# Practical 3 - Question 9: Triangle classification

# I check whether the sides form a valid triangle before naming its type.

# I start with an empty entered numbers list.
entered_numbers = []

# I convert each separated input into a number before storing it.
for number_text in input('Three sides: ').split():
    entered_numbers.append(float(number_text))
a, b, c = entered_numbers

# I check this condition to decide which step should run.
if min(a, b, c) <= 0 or a + b <= c or a + c <= b or (b + c <= a):
    print('Invalid triangle')
elif a == b == c:
    print('Equilateral')
elif a == b or b == c or a == c:
    print('Isosceles')
else:
    print('Scalene')
