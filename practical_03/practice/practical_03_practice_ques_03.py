# Practical 3 - Practice Question 3: E-commerce bill

amount = float(input("Purchase amount (INR): "))
if amount < 0:
    print("Amount cannot be negative.")
else:
    # "Above" uses strict comparisons, unlike inclusive thresholds.
    if amount > 5000:
        rate = 0.15
    elif amount > 2000:
        rate = 0.10
    else:
        rate = 0
    print(f"Discount: INR {amount * rate:.2f}\nFinal bill: INR {amount * (1 - rate):.2f}")
