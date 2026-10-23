# Practical 7 - Question 8: Tuple methods

# count gives occurrences; index gives the first 0-based position.
values = (10, 20, 10, 30)
print("Count of 10:", values.count(10))
print("Index of 20:", values.index(20))
try:
    print(values.index(99))
except ValueError:
    print("ValueError: 99 is not in the tuple.")
