# Practical 9 - Question 11: Menu with functions

# I keep each menu operation in a separate function.

from math import isqrt

# This function takes two numbers and returns their sum.
def add(a, b):
    # I return the result so it can be used by the calling code.
    return a + b

# I check the possible divisors inside this function.
def is_prime(n):
    if n < 2:
        return False
    # I try the possible divisors one by one.
    for divisor in range(2, isqrt(n) + 1):
        # I use the remainder to check this condition.
        if n % divisor == 0:
            return False
    # I return the result so it can be used by the calling code.
    return True

# I use this function to calculate the factorial.
def factorial(n):
    result = 1
    # I repeat this step for each value in the sequence.
    for i in range(1, n + 1):
        result *= i
    # I return the result so it can be used by the calling code.
    return result

# I display the result clearly.
print('1. Addition\n2. Prime check\n3. Factorial')

# First, I take the required input from the user.
choice = input('Choice: ')

# I check this condition to decide which step should run.
if choice == '1':
    # I start with an empty entered numbers list.
    entered_numbers = []
    # I convert each separated input into a number before storing it.
    for number_text in input('Two numbers: ').split():
        entered_numbers.append(float(number_text))
    a, b = entered_numbers
    print('Sum:', add(a, b))
elif choice == '2':
    if is_prime(int(input('Integer: '))):
        prime_result = 'Prime'
    else:
        prime_result = 'Not prime'
    print(prime_result)
elif choice == '3':
    # I take the input needed in this step.
    n = int(input('Nonnegative integer: '))
    if n >= 0:
        print('Factorial:', factorial(n))
    else:
        print('Invalid negative integer')
else:
    print('Invalid choice')
