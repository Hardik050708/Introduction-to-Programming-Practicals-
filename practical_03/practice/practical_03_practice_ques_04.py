# Practical 3 - Practice Question 4: Nested voting eligibility

# Nested conditions require both adult age and Indian nationality.
age = int(input("Age: "))
nationality = input("Nationality: ").strip().lower()
if age >= 18:
    if nationality == "indian":
        print("Eligible to vote")
    else:
        print("Not eligible: nationality must be Indian.")
else:
    print("Not eligible: age must be at least 18.")
