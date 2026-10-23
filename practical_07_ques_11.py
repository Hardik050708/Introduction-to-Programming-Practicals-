# Practical 7 - Question 11: Iteration and summation

for values in ([10, 20, 30], (10, 20, 30)):
    total = 0
    for value in values:
        print(value, end=" ")
        total += value
    print("\nSum:", total)  # Both sequence types support the same iteration.
