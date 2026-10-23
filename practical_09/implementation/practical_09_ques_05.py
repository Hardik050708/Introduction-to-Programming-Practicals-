# Practical 9 - Question 5: Built-in functions

numbers = [10, 20, 30, 40]
text = "Python"
print("List len, sum, max, min:", len(numbers), sum(numbers), max(numbers), min(numbers))
print("String len, max, min:", len(text), max(text), min(text))
# sum() needs numeric values; it cannot add the characters of a string.
total, count = 0, 0
largest = smallest = numbers[0]
for number in numbers:
    total += number
    count += 1
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print("Manual len, sum, max, min:", count, total, largest, smallest)
