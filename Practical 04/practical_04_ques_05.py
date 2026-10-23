# Practical 4 - Question 5: Multiplication table

# I multiply the number by 1 to 10 to make its table.

# First, I take the required input from the user.
n = int(input('Number: '))

# I repeat this step for each value in the sequence.
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
