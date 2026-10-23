# Practical 9 - Question 6: Process lists with a function

# I write one function to find the sum and largest value for different lists.

# I calculate the total and largest value inside this function.
def analyze(numbers):
    if not numbers:
        return (0, None)
    # I start total at zero before counting or adding anything.
    total = 0
    largest = numbers[0]
    # I repeat this step for each value in the sequence.
    for number in numbers:
        total += number
        if number > largest:
            largest = number
    # I return the result so it can be used by the calling code.
    return (total, largest)

# I repeat this step for each value in the sequence.
for values in ([10, 20, 30], [-5, -2, -9], []):
    total, largest = analyze(values)
    print(f'{values}: sum={total}, largest={largest}')
