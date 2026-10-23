# Practical 7 - Question 6: Remove list elements

numbers = [10, 20, 30, 40]
numbers.remove(20)  # remove deletes the first matching value.
print("Popped:", numbers.pop())  # pop returns the last element by default.
print("Remaining:", numbers)
try:
    numbers.remove(99)
except ValueError:
    print("ValueError: 99 is not present.")
