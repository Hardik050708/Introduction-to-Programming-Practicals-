# Practical 1 - Question 9: Data type based calculator

# I take two values as text because input() returns strings.
first_input = input("First value (number or text): ")
second_input = input("Second value (number or text): ")

# I try integer conversion first, then float, and otherwise keep the text.
try:
    first_value = int(first_input)
except ValueError:
    try:
        first_value = float(first_input)
    except ValueError:
        first_value = first_input

try:
    second_value = int(second_input)
except ValueError:
    try:
        second_value = float(second_input)
    except ValueError:
        second_value = second_input

print("Types:", type(first_value).__name__, type(second_value).__name__)

# Two numbers are added, while two strings are joined together.
if isinstance(first_value, (int, float)) and isinstance(second_value, (int, float)):
    answer = first_value + second_value
    print("Sum:", answer)
elif isinstance(first_value, str) and isinstance(second_value, str):
    answer = first_value + second_value
    print("Concatenation:", answer)
else:
    print("Invalid combination: enter two numbers or two strings.")
