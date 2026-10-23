# Practical 3 - Question 7: Conditional calculator

# Select the arithmetic operation by matching the entered operator.
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+, -, *, /): ").strip()
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid operator")
