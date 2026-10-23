# Practical 2 - Question 5: Salary breakdown

basic = float(input("Basic salary (INR): "))
if basic < 0:
    print("Salary cannot be negative.")
else:
    hra, da = basic * 0.20, basic * 0.10
    net = basic + hra + da  # No deductions are specified.
    print(f"Basic: INR {basic:.2f}\nHRA: INR {hra:.2f}\nDA: INR {da:.2f}\nNet: INR {net:.2f}")
