# Practical 2 - Question 8: Multiple inputs in one line

# I take all three inputs in one line, as asked in the manual.
a, b, c = input("Enter three numbers: ").split()
a = float(a)
b = float(b)
c = float(c)

# I find the sum and product after converting the inputs.
total = a + b + c
product = a * b * c

print(f"Sum: {total:g}")
print(f"Product: {product:g}")
