# Practical 9 - Question 6: Process lists with a function

# Accumulate the list sum while tracking its largest value.
def analyze(numbers):
    if not numbers:
        return 0, None
    total = 0
    largest = numbers[0]
    for number in numbers:
        total += number
        if number > largest:
            largest = number
    return total, largest

for values in ([10, 20, 30], [-5, -2, -9], []):
    total, largest = analyze(values)
    print(f"{values}: sum={total}, largest={largest}")
