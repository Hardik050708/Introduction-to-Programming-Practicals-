# Practical 2 - Practice Question 7: Simple interest EMI estimate

principal, months, annual_rate = 500000, 24, 12
interest = principal * annual_rate * (months / 12) / 100
# This is a simple-interest estimate, not a reducing-balance bank EMI.
emi = (principal + interest) / months
print(f"Interest: INR {interest:.2f}\nMonthly EMI: INR {emi:.2f}")
