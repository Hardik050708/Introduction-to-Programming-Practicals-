# Practical 9 - Practice Question 3: Recursive digit sum

# Add the last digit to the recursive sum of the remaining digits.
def digit_sum(pin):
    pin = abs(pin)
    if pin < 10:
        return pin
    return pin % 10 + digit_sum(pin // 10)

print("Digit sum:", digit_sum(482931))
