# Practical 9 - Question 8: Recursive Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Terms (0-20): "))
if not 0 <= n <= 20:
    print("Use 0 to 20 terms for this recursive demonstration.")
else:
    print("Recursive:", [fibonacci(i) for i in range(n)])
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    print("Iterative:", sequence)
# Naive recursion repeats work exponentially; iteration takes linear time.
