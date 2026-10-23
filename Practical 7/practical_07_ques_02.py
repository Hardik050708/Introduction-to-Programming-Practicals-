# Practical 7 - Question 2: Positive and negative indexing

# I use positive and negative indices to access the same positions.

# I repeat this step for each value in the sequence.
for values in ([10, 20, 30, 40, 50], ('a', 'b', 'c', 'd', 'e')):
    print('First:', values[0], values[-5])
    print('Last:', values[4], values[-1])
    print('Middle:', values[2], values[-3])
