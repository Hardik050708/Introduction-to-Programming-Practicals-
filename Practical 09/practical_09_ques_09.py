# Practical 9 - Question 9: Functions calling functions

# I keep input, processing and output in separate functions.
def read_numbers():
    numbers = list(map(float, input("Numbers separated by spaces: ").split()))
    return numbers


def process(numbers):
    total = sum(numbers)
    return total


def display(total):
    print("Total:", total)


# I call each function in order from the main function.
def main():
    numbers = read_numbers()
    total = process(numbers)
    display(total)


main()
