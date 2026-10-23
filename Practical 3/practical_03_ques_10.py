# Practical 3 - Question 10: Menu driven conditions

# I use the menu choice to decide which calculation should run.

# I display the result clearly.
print('1. Even/Odd\n2. Largest of three\n3. Grade')

# First, I take the required input from the user.
choice = input('Choice: ').strip()

# I check this condition to decide which step should run.
if choice == '1':
    # I take the input needed in this step.
    n = int(input('Integer: '))
    # I use the remainder to check this condition.
    if n % 2 == 0:
        parity_result = 'Even'
    else:
        parity_result = 'Odd'
    print(parity_result)
elif choice == '2':
    # I start with an empty entered numbers list.
    entered_numbers = []
    # I convert each separated input into a number before storing it.
    for number_text in input('Three numbers: ').split():
        entered_numbers.append(float(number_text))
    a, b, c = entered_numbers
    if a >= b and a >= c:
        print('Largest:', a)
    elif b >= c:
        print('Largest:', b)
    else:
        print('Largest:', c)
elif choice == '3':
    # I take the input needed in this step.
    marks = float(input('Marks (0-100): '))
    if not 0 <= marks <= 100:
        print('Invalid marks')
    elif marks >= 90:
        print('Grade: A')
    elif marks >= 75:
        print('Grade: B')
    elif marks >= 50:
        print('Grade: C')
    else:
        print('Fail')
else:
    print('Invalid choice')
