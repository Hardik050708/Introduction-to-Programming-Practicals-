# Practical 5 - Question 7: Sum valid inputs

# Zero stops input, negative values are skipped, and positive values accumulate.
total = 0
while True:
    n = float(input("Number (0 to stop): "))
    if n == 0:
        break
    if n < 0:
        continue
    total += n
print("Sum:", total)
