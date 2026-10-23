# Practical 1 - Question 1: Variable creation and naming rules

name = "Asha"
age = 18
marks = 91.5
city = "Pune"
print(name, age, marks, city)
# Names cannot start with digits, use keywords, or contain a hyphen.
for code in ['1name = "Asha"', 'class = 18', 'my-name = "Asha"']:
    try:
        compile(code, "<example>", "exec")
    except SyntaxError:
        print(code, "-> SyntaxError")
first_name, class_number, my_name = "Asha", 12, "Asha"
print(first_name, class_number, my_name)
