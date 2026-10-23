# Practical 1 - Question 8: Swapping variables

a, b = 10, 20
# A temporary variable preserves the first value.
temp = a
a = b
b = temp
print("Third variable:", a, b)
a, b = 10, 20
# Tuple unpacking swaps both values in one statement.
a, b = b, a
print("Tuple unpacking:", a, b)
