# Practical 7 - Question 6: Remove list elements

# I compare removal by value with removal using pop().

numbers = [10, 20, 30, 40]

# I remove the first matching item.
numbers.remove(20)

# I display the result clearly.
print('Popped:', numbers.pop())
print('Remaining:', numbers)

# I use try-except so the expected error does not stop the example.
try:
    numbers.remove(99)
except ValueError:
    print('ValueError: 99 is not present.')
