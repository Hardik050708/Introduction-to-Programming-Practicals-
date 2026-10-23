# Practical 4 - Practice Question 9: Predict Fibonacci output

a, b = 0, 1
for i in range(5):
    print(a, end=" ")  # Output: 0 1 1 2 3
    a, b = b, a + b
print()
