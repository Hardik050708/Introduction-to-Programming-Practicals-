# Practical 3 - Practice Question 2: Loan approval

# Salary is inclusive at 30000, but the credit score must be strictly above 700.
salary = float(input("Salary: "))
score = int(input("Credit score: "))
print("Approved" if salary >= 30000 and score > 700 else "Not approved")
