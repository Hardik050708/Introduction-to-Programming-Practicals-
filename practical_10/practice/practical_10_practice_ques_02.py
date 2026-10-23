# Practical 10 - Practice Question 2: Student ID masking

# Keep four characters at each end and replace the middle with four stars.
student_id = "STU2026CS1098"
print("First four:", student_id[:4])
print("Last four:", student_id[-4:])
print("Masked:", student_id[:4] + "****" + student_id[-4:])
