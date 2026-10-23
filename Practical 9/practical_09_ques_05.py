# Practical 9 - Question 5: Built-in functions

# I compare the built-in answers with values found using a loop.

numbers = [10, 20, 30, 40]
text = 'Python'

# I display the result clearly.
print('List len, sum, max, min:', len(numbers), sum(numbers), max(numbers), min(numbers))
print('String len, max, min:', len(text), max(text), min(text))

# I start total at zero before counting or adding anything.
total = 0

# I start count at zero before counting or adding anything.
count = 0
largest = numbers[0]
smallest = largest

# I repeat this step for each value in the sequence.
for number in numbers:
    total += number
    count += 1
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

# I display the result clearly.
print('Manual len, sum, max, min:', count, total, largest, smallest)
