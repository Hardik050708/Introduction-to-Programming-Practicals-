# Practical 2 - Practice Question 1: Electricity bill

units = float(input("Units consumed: "))
if units < 0:
    print("Units cannot be negative.")
else:
    fixed = 150  # The first 100 units are covered by the fixed charge.
    variable = max(0, units - 100) * 6
    print(f"Fixed: INR {fixed:.2f}\nVariable: INR {variable:.2f}\nTotal: INR {fixed + variable:.2f}")
