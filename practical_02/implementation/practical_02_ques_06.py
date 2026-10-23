# Practical 2 - Question 6: Area and perimeter

# Use length * width for rectangle area and pi * radius squared for circle area.
from math import pi
length = float(input("Rectangle length: "))
width = float(input("Rectangle width: "))
radius = float(input("Circle radius: "))
if min(length, width, radius) < 0:
    print("Dimensions cannot be negative.")
else:
    print(f"Rectangle area: {length * width:.2f} square units")
    print(f"Rectangle perimeter: {2 * (length + width):.2f} units")
    print(f"Circle area: {pi * radius ** 2:.2f} square units")
    print(f"Circle circumference: {2 * pi * radius:.2f} units")
