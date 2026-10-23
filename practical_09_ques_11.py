# Practical 9 - Question 11: Menu with functions

# Keep each calculation in a function and select one using the menu.
from math import isqrt

def add(a, b):
    return a + b

def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("1. Addition\n2. Prime check\n3. Factorial")
choice = input("Choice: ")
if choice == "1":
    a, b = map(float, input("Two numbers: ").split())
    print("Sum:", add(a, b))
elif choice == "2":
    print("Prime" if is_prime(int(input("Integer: "))) else "Not prime")
elif choice == "3":
    n = int(input("Nonnegative integer: "))
    if n >= 0:
        print("Factorial:", factorial(n))
    else:
        print("Invalid negative integer")
else:
    print("Invalid choice")
