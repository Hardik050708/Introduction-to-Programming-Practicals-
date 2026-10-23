# Practical 4 - Question 8: Prime checking

from math import isqrt
n = int(input("Integer: "))
is_prime = n >= 2
# Every composite has a divisor no larger than its square root.
for divisor in range(2, isqrt(max(n, 0)) + 1):
    if n % divisor == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not prime")
