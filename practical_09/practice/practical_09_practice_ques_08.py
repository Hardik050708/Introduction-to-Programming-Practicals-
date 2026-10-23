# Practical 9 - Practice Question 8: Predict recursive factorial

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(4))  # Output: 24
