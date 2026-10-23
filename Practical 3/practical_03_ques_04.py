# Practical 3 - Question 4: Nested voting conditions

# Check age first, then check nationality inside the age-qualified branch.
age = int(input("Age: "))
nationality = input("Nationality: ").strip().lower()
if age >= 18:
    if nationality == "indian":
        print("Eligible to vote")
    else:
        print("Not eligible: nationality must be Indian.")
else:
    print("Not eligible: age must be at least 18.")
