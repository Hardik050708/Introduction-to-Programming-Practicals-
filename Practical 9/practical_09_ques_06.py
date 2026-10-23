# Practical 9 - Question 6: Process lists with a function

# I define a function to calculate the sum and largest item in a list.
def analyze(numbers):
    if len(numbers) == 0:
        return 0, None

    total = 0
    largest = numbers[0]
    for number in numbers:
        total = total + number
        if number > largest:
            largest = number
    return total, largest

# I call the same function for different lists to show its reuse.
first_list = [10, 20, 30]
first_total, first_largest = analyze(first_list)
print(f"{first_list}: sum={first_total}, largest={first_largest}")

second_list = [-5, -2, -9]
second_total, second_largest = analyze(second_list)
print(f"{second_list}: sum={second_total}, largest={second_largest}")

empty_list = []
empty_total, empty_largest = analyze(empty_list)
print(f"{empty_list}: sum={empty_total}, largest={empty_largest}")
