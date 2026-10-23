# Practical 4 - Question 4: Factorial using for and while

n = int(input("Nonnegative integer: "))
if n < 0:
    print("Factorial is undefined for negative integers.")
else:
    for_result = 1
    for i in range(1, n + 1):
        for_result *= i
    while_result, i = 1, 1
    while i <= n:
        while_result *= i
        i += 1
    print("For factorial:", for_result)
    print("While factorial:", while_result)  # Both loops also give 0! = 1.
