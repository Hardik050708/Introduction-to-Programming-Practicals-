# Practical 7 - Question 11: Iteration and summation

numbers = [10, 20, 30]
fixed_numbers = (10, 20, 30)

# This question asks for iteration, so I use a loop for the list.
list_total = 0
for number in numbers:
    print(number, end=" ")
    list_total = list_total + number
print("\nSum:", list_total)

# I repeat the same calculation for the tuple to compare iteration.
tuple_total = 0
for number in fixed_numbers:
    print(number, end=" ")
    tuple_total = tuple_total + number
print("\nSum:", tuple_total)
