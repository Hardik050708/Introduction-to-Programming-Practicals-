# Practical 2 - Question 8: Multiple inputs in one line

# map converts the three split inputs before computing their sum and product.
a, b, c = map(float, input("Enter three numbers: ").split())
print(f"Sum: {a + b + c:g}")
print(f"Product: {a * b * c:g}")
