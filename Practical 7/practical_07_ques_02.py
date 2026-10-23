# Practical 7 - Question 2: Positive and negative indexing

# Positive indices count from the start and negative indices from the end.
for values in ([10, 20, 30, 40, 50], ("a", "b", "c", "d", "e")):
    print("First:", values[0], values[-5])
    print("Last:", values[4], values[-1])
    print("Middle:", values[2], values[-3])
