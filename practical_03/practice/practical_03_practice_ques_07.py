# Practical 3 - Practice Question 7: Scholarship eligibility

# Both the strict marks cutoff and strict income limit must be satisfied.
marks = float(input("Marks (0-100): "))
income = float(input("Family annual income (INR): "))
if not 0 <= marks <= 100 or income < 0:
    print("Invalid marks or income")
else:
    print("Eligible" if marks > 85 and income < 300000 else "Not eligible")
