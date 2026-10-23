# Practical 1 - Question 1: Variable creation and naming rules

# I have used valid variable names and checked why the invalid names give errors.

name = 'Asha'
age = 18
marks = 91.5
city = 'Pune'

# I display the result clearly.
print(name, age, marks, city)

# I repeat this step for each value in the sequence.
for code in ['1name = "Asha"', 'class = 18', 'my-name = "Asha"']:
    # I use try-except so the expected error does not stop the example.
    try:
        compile(code, '<example>', 'exec')
    except SyntaxError:
        print(code, '-> SyntaxError')
first_name = 'Asha'
class_number = 12
my_name = 'Asha'

# I display the result clearly.
print(first_name, class_number, my_name)
