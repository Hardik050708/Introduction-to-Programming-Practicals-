# Practical 7 - Question 3: List and tuple slicing

for values in ([1, 2, 3, 4, 5, 6], (1, 2, 3, 4, 5, 6)):
    print("First three:", values[:3])
    print("Last two:", values[-2:])
    print("Alternate:", values[::2])  # Slicing preserves the sequence type.
