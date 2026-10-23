# Practical 4 - Question 8: Prime checking

# I test divisors only up to the square root to avoid extra checks.

from math import isqrt

# First, I take the required input from the user.
n = int(input('Integer: '))
is_prime = n >= 2

# I try the possible divisors one by one.
for divisor in range(2, isqrt(max(n, 0)) + 1):
    # I use the remainder to check this condition.
    if n % divisor == 0:
        is_prime = False
        # I stop this loop as soon as the required condition is met.
        break

# I choose the message using the prime-check result.
if is_prime:
    prime_result = 'Prime'
else:
    prime_result = 'Not prime'

# I display the result clearly.
print(prime_result)
