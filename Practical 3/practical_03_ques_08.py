# Practical 3 - Question 8: Purchase discount

# I find the discount rate first, then subtract the discount from the amount.

# I treat 1000 and 2000 as inclusive discount thresholds.

# First, I take the required input from the user.
amount = float(input('Purchase amount (INR): '))

# I check this condition to decide which step should run.
if amount < 0:
    print('Amount cannot be negative.')
else:
    if amount >= 2000:
        rate = 0.2
    elif amount >= 1000:
        rate = 0.1
    else:
        rate = 0
    print(f'Discount: INR {amount * rate:.2f}\nFinal amount: INR {amount * (1 - rate):.2f}')
