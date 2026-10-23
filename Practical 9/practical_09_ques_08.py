# Practical 9 - Question 8: Recursive Fibonacci

# I compare recursive Fibonacci with the faster iterative approach.

# Recursive Fibonacci repeats calculations, so I limit this demo to 20 terms.

# I return the two base values directly and use recursion for later terms.
def fibonacci(n):
    if n <= 1:
        return n
    # I return the result so it can be used by the calling code.
    return fibonacci(n - 1) + fibonacci(n - 2)

# First, I take the required input from the user.
n = int(input('Terms (0-20): '))

# I check this condition to decide which step should run.
if not 0 <= n <= 20:
    print('Use 0 to 20 terms for this recursive demonstration.')
else:
    # I start with an empty recursive sequence list.
    recursive_sequence = []
    # I repeat this step for each value in the sequence.
    for i in range(n):
        recursive_sequence.append(fibonacci(i))
    print('Recursive:', recursive_sequence)
    # I start with an empty sequence list.
    sequence = []
    a = 0
    b = 1
    # I repeat this step for each value in the sequence.
    for i in range(n):
        sequence.append(a)
        # I find the next term before changing the previous two terms.
        next_term = a + b
        a = b
        b = next_term
    print('Iterative:', sequence)
