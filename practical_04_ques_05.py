# Practical 4 - Question 5: Multiplication table

# Multiply the chosen number by each integer from 1 through 10.
n = int(input("Number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
