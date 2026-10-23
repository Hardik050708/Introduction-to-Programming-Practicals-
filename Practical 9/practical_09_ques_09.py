# Practical 9 - Question 9: Functions calling functions

# I keep input, processing and output in separate functions.

# I keep the input step in its own function.
def read_numbers():
    # I start with an empty entered numbers list.
    entered_numbers = []
    # I convert each separated input into a number before storing it.
    for number_text in input('Numbers separated by spaces: ').split():
        entered_numbers.append(float(number_text))
    # I return the result so it can be used by the calling code.
    return list(entered_numbers)

# I keep the calculation separate from input and output.
def process(numbers):
    return sum(numbers)

# I use this function only to show the final result.
def display(total):
    print('Total:', total)

# I call the required functions here in the correct order.
def main():
    numbers = read_numbers()
    total = process(numbers)
    display(total)

# I call main() to start the complete program.
main()
