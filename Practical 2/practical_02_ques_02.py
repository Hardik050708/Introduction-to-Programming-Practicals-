# Practical 2 - Question 2: Numeric input handling

# Convert both inputs to floats before applying numeric arithmetic.
x = input("First number: ")
y = input("Second number: ")
print("Without conversion (concatenation):", x + y)
a, b = float(x), float(y)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Undefined: division by zero")
