# Practical 2 - Question 5: Salary breakdown

# I calculate HRA and DA separately and add both to the basic salary.

# No deductions are given, so I add the allowances to the basic salary.

# First, I take the required input from the user.
basic = float(input('Basic salary (INR): '))

# I check this condition to decide which step should run.
if basic < 0:
    print('Salary cannot be negative.')
else:
    # I multiply the values and store the answer in hra.
    hra = basic * 0.2
    # I multiply the values and store the answer in da.
    da = basic * 0.1
    # I add the values and store the answer in net.
    net = basic + hra + da
    print(f'Basic: INR {basic:.2f}\nHRA: INR {hra:.2f}\nDA: INR {da:.2f}\nNet: INR {net:.2f}')
