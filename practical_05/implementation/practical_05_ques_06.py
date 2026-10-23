# Practical 5 - Question 6: Skip negative inputs

numbers = list(map(float, input("Numbers: ").split()))
for n in numbers:
    if n < 0:
        continue
    if n > 0:  # Zero is not positive.
        print(n)
