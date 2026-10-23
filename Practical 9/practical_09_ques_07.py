# Practical 9 - Question 7: Recursive factorial

def factorial(n):
    print(f"factorial({n})")  # Trace each recursive call.
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Integer (0-100): "))
if not 0 <= n <= 100:
    print("Use 0 to 100 for this recursion demonstration.")
else:
    recursive = factorial(n)
    iterative = 1
    for i in range(1, n + 1):
        iterative *= i
    print("Recursive:", recursive)
    print("Iterative:", iterative)
