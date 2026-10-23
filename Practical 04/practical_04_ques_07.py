# Practical 4 - Question 7: Count digits by parity

# I count each digit and check whether that digit is even or odd.

# Zero has one digit, and that digit is even.

# First, I take the required input from the user.
n = abs(int(input('Integer: ')))

# I start total at zero before counting or adding anything.
total = 0
even = total
odd = total

# I check this condition to decide which step should run.
if n == 0:
    total = 1
    even = total

# I repeat the steps until the stopping condition is reached.
while n > 0:
    # I find the remainder and store the answer in digit.
    digit = n % 10
    total += 1
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

# I display the result clearly.
print('Total digits:', total)
print('Even digits:', even)
print('Odd digits:', odd)
