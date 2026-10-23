# Practical 4 - Question 9: Fibonacci iteration

n = int(input("Number of terms: "))
if n < 0:
    print("Count cannot be negative.")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Advance using the previous pair.
    print()
