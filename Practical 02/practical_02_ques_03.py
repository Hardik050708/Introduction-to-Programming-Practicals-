# Practical 2 - Question 3: Evaluate expressions

# I accept three numbers and convert each one separately.
a, b, c = input("Three numbers separated by spaces: ").split()
a = float(a)
b = float(b)
c = float(c)

# I calculate the three results using the expressions in the question.
total = a + b + c
average = total / 3
expression_result = (a + b) * c / 2

print("Sum:", total)
print("Average:", average)
print("(a + b) * c / 2:", expression_result)
