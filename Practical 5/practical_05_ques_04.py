# Practical 5 - Question 4: Search a list

# I stop the search at the first match and display its position.

# I start with an empty numbers list.
numbers = []

# I convert each separated input into a number before storing it.
for number_text in input('Numbers separated by spaces: ').split():
    numbers.append(int(number_text))

# First, I take the required input from the user.
target = int(input('Search number: '))

# I repeat this step for each value in the sequence.
for i, number in enumerate(numbers):
    if number == target:
        # I add the values and store the answer in position.
        position = i + 1
        print('Position:', position)
        # I stop this loop as soon as the required condition is met.
        break
else:
    print('Not found')
