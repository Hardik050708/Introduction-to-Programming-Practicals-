# Practical 1 - Question 9: Data type based calculator

from ast import literal_eval

def detect(text):
    # Parse literals safely; plain words are treated as strings.
    try:
        return literal_eval(text)
    except (ValueError, SyntaxError):
        return text

a = detect(input("First value (number or text): "))
b = detect(input("Second value (number or text): "))
print("Types:", type(a).__name__, type(b).__name__)
if type(a) in (int, float) and type(b) in (int, float):
    print("Sum:", a + b)
elif isinstance(a, str) and isinstance(b, str):
    print("Concatenation:", a + b)
else:
    print("Invalid combination: enter two numbers or two strings.")
