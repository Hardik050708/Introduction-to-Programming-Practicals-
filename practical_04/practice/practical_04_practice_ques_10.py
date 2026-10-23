# Practical 4 - Practice Question 10: Predict nested pattern

# Output rows contain one, two, and three stars.
for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()
