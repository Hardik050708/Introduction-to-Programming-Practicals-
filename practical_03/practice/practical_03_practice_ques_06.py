# Practical 3 - Practice Question 6: Age group

age = int(input("Age: "))
# Assumed ranges: 0-12 child, 13-19 teen, 20-59 adult, 60+ senior.
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
