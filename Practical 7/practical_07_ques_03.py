# Practical 7 - Question 3: List and tuple slicing

# I try the same slices on a list and a tuple.

# I repeat this step for each value in the sequence.
for values in ([1, 2, 3, 4, 5, 6], (1, 2, 3, 4, 5, 6)):
    print('First three:', values[:3])
    print('Last two:', values[-2:])
    print('Alternate:', values[::2])
