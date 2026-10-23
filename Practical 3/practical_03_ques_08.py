# Practical 3 - Question 8: Purchase discount

amount = float(input("Purchase amount (INR): "))
# The stated thresholds are inclusive: 2000 and 1000 qualify.
if amount < 0:
    print("Amount cannot be negative.")
else:
    if amount >= 2000:
        rate = 0.20
    elif amount >= 1000:
        rate = 0.10
    else:
        rate = 0
    print(f"Discount: INR {amount * rate:.2f}\nFinal amount: INR {amount * (1 - rate):.2f}")
