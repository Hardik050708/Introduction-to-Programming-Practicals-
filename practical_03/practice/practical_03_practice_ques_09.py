# Practical 3 - Practice Question 9: Systolic blood pressure category

systolic = float(input("Systolic reading (mmHg): "))
# Classroom systolic-only ranges: <120, 120-129, 130-139, >=140.
if systolic <= 0:
    print("Invalid reading")
elif systolic < 120:
    print("Normal")
elif systolic < 130:
    print("Elevated")
elif systolic < 140:
    print("High Stage 1")
else:
    print("High Stage 2")
