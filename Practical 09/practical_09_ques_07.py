# Practical 9 - Question 7: Recursive factorial

# I use a base case to stop recursion and compare the answer with a loop.

# I keep the demo input at 0 to 100 to avoid too many recursive calls.

# I use this function to calculate the factorial.
def factorial(n):
    print(f'factorial({n})')
    if n <= 1:
        return 1
    # I return the result so it can be used by the calling code.
    return n * factorial(n - 1)

# First, I take the required input from the user.
n = int(input('Integer (0-100): '))

# I check this condition to decide which step should run.
if not 0 <= n <= 100:
    print('Use 0 to 100 for this recursion demonstration.')
else:
    recursive = factorial(n)
    iterative = 1
    # I repeat this step for each value in the sequence.
    for i in range(1, n + 1):
        iterative *= i
    print('Recursive:', recursive)
    print('Iterative:', iterative)
