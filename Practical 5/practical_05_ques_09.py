# Practical 5 - Question 9: Pass in an empty block

for number in range(1, 6):
    if number % 2 == 0:
        pass  # Placeholder does nothing but keeps the block syntactically valid.
    print(number)  # pass neither skips nor stops this statement.
