# Practical 1 - Question 4: Data type identification

# I convert each input to its required type and show a small summary.

# First, I take the required input from the user.
number = int(input('Integer: '))
decimal = float(input('Float: '))
text = input('String: ')
answer = input('Boolean (true/false): ').strip().lower()

# I check this condition to decide which step should run.
if answer not in ('true', 'false'):
    print('Enter true or false for the Boolean.')
else:
    flag = answer == 'true'
    print(f"{'Value':<20} Type")
    # I repeat this step for each value in the sequence.
    for value in (number, decimal, text, flag):
        print(f'{str(value):<20} {type(value).__name__}')
