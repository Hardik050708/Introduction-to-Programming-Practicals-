# Practical 8 - Practice Question 1: Attendance dictionary

# Update statuses by student ID, then count values equal to Present.
attendance = {"S101":"Present", "S102":"Absent", "S103":"Present", "S104":"Late"}
attendance["S104"] = "Present"
attendance["S105"] = "Present"
print(attendance)
print("Present students:", list(attendance.values()).count("Present"))
