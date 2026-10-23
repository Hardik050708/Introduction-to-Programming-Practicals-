# Practical 5 - Question 6: Skip negative inputs

# I skip negative values and display only the positive numbers.

# I start with an empty numbers list.
numbers = []

# I convert each separated input into a number before storing it.
for number_text in input('Numbers: ').split():
    numbers.append(float(number_text))

# I repeat this step for each value in the sequence.
for n in numbers:
    # I check the input before using it in the calculation.
    if n < 0:
        # I skip this value and continue with the next one.
        continue
    if n > 0:
        print(n)
