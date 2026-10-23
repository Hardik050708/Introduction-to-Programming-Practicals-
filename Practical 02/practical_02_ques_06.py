# Practical 2 - Question 6: Area and perimeter

# I calculate the area and boundary length using the formulas for each shape.

from math import pi

# First, I take the required input from the user.
length = float(input('Rectangle length: '))
width = float(input('Rectangle width: '))
radius = float(input('Circle radius: '))

# I check this condition to decide which step should run.
if min(length, width, radius) < 0:
    print('Dimensions cannot be negative.')
else:
    print(f'Rectangle area: {length * width:.2f} square units')
    print(f'Rectangle perimeter: {2 * (length + width):.2f} units')
    print(f'Circle area: {pi * radius ** 2:.2f} square units')
    print(f'Circle circumference: {2 * pi * radius:.2f} units')
