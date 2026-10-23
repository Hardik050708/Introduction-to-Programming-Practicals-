# Practical 4 - Question 3: Sum and average with a loop

n = int(input("How many numbers? "))
if n <= 0:
    print("Count must be positive.")
else:
    total = 0
    for i in range(n):
        total += float(input(f"Number {i + 1}: "))  # Accumulate each input.
    print("Sum:", total)
    print("Average:", total / n)
