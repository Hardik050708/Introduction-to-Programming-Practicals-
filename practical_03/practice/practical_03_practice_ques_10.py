# Practical 3 - Practice Question 10: Employee bonus

# Choose the bonus rate by completed service years, then apply it to salary.
years = int(input("Completed service years: "))
salary = float(input("Salary (INR): "))
if years < 0 or salary < 0:
    print("Invalid years or salary")
else:
    if years >= 10:
        rate = 0.20
    elif years >= 5:
        rate = 0.10
    else:
        rate = 0
    print(f"Bonus rate: {rate:.0%}\nBonus: INR {salary * rate:.2f}")
