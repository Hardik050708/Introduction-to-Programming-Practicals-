# Practical 2 - Practice Question 6: Topper position

marks = list(map(float, input("Marks of five students: ").split()))
if len(marks) != 5:
    print("Enter exactly five marks.")
else:
    highest = max(marks)
    positions = [i + 1 for i, mark in enumerate(marks) if mark == highest]
    print("Topper marks:", highest)
    print("Student position(s):", positions)  # Positions start at 1; ties are included.
