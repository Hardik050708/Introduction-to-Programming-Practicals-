# Practical 9 - Question 4: Default and keyword arguments

def greet(name="Student", message="Hello"):
    print(message, name)

greet()  # Defaults apply when arguments are omitted.
greet("Asha", "Welcome")  # Positional arguments follow parameter order.
greet(message="Welcome", name="Asha")  # Keyword arguments can change order.
