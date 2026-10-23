# Practical 4 - Practice Question 8: Correct factorial accumulator

n = 5
fact = 1  # Starting at zero would make every product zero.
for i in range(1, n + 1):
    fact *= i
print(fact)
