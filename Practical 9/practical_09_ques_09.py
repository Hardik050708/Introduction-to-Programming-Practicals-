# Practical 9 - Question 9: Functions calling functions

def read_numbers():
    return list(map(float, input("Numbers separated by spaces: ").split()))

def process(numbers):
    return sum(numbers)

def display(total):
    print("Total:", total)

def main():
    display(process(read_numbers()))  # Compose input, processing, and output functions.

main()
