# Practical 9 - Question 4: Default and keyword arguments

# I call the function using defaults, positional arguments and keyword arguments.

# I define the greeting here so I can reuse it.
def greet(name='Student', message='Hello'):
    print(message, name)
greet()
greet('Asha', 'Welcome')
greet(message='Welcome', name='Asha')
