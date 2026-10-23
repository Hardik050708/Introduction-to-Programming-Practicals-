# Practical 2 - Question 10: Error analysis

# Catch the demonstration errors so the corrected examples also run.
try:
    print(10 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError: the divisor cannot be zero.")
try:
    print("10" + 5)
except TypeError:
    print("TypeError: convert strings before numeric addition.")
divisor = 0
if divisor != 0:
    print(10 / divisor)
else:
    print("Division prevented: divisor is zero.")
print("Correct addition:", int("10") + 5)
