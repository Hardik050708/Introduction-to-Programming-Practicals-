# Practical 7 - Question 3: List and tuple slicing

numbers = [1, 2, 3, 4, 5, 6]
fixed_numbers = (1, 2, 3, 4, 5, 6)

# I use the same slices on the list and tuple to compare the results.
print("First three:", numbers[:3])
print("Last two:", numbers[-2:])
print("Alternate:", numbers[::2])

print("First three:", fixed_numbers[:3])
print("Last two:", fixed_numbers[-2:])
print("Alternate:", fixed_numbers[::2])

# A list slice remains a list, and a tuple slice remains a tuple.
