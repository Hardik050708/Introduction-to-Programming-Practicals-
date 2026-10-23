# Practical 5 - Question 5: First divisible number

# Stop at the first matching multiple; a loop else handles no match.
n = int(input("Divisor: "))
if n == 0:
    print("Divisor cannot be zero.")
else:
    for number in range(1, 101):
        if number % n == 0:
            print("First divisible number:", number)
            break
    else:
        print("No divisible number between 1 and 100.")
