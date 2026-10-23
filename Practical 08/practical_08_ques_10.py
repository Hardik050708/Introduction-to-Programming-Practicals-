# Practical 8 - Question 10: Merge dictionaries

# I use update() to merge dictionaries and observe the overwritten key.

first = {'a': 1, 'b': 2}
second = {'b': 20, 'c': 3}

# I merge the new dictionary entries into the first dictionary.
first.update(second)

# I display the result clearly.
print(first)
