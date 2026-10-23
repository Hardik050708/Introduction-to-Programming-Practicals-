# Practical 7 - Question 2: Positive and negative indexing

# I create the list and tuple before accessing their elements.
numbers = [10, 20, 30, 40, 50]
letters = ("a", "b", "c", "d", "e")

# Positive indices start at zero, and negative indices start from the end.
print("First:", numbers[0], numbers[-5])
print("Last:", numbers[4], numbers[-1])
print("Middle:", numbers[2], numbers[-3])

print("First:", letters[0], letters[-5])
print("Last:", letters[4], letters[-1])
print("Middle:", letters[2], letters[-3])
