# Practical 3 - Practice Question 1: Placement eligibility

# Both the minimum CGPA and minimum attendance must be satisfied.
cgpa = float(input("CGPA (0-10): "))
attendance = float(input("Attendance (%): "))
if not 0 <= cgpa <= 10 or not 0 <= attendance <= 100:
    print("Invalid CGPA or attendance")
else:
    print("Eligible" if cgpa >= 7 and attendance >= 75 else "Not eligible")
