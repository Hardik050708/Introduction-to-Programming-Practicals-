# Practical 2 - Question 3: Evaluate expressions

# Parentheses group the sum before multiplication and division.
a, b, c = map(float, input("Three numbers separated by spaces: ").split())
print("Sum:", a + b + c)
print("Average:", (a + b + c) / 3)
print("(a + b) * c / 2:", (a + b) * c / 2)
