# Practical 2 - Question 9: Three subject grading

# Three subjects out of 100 give percentage = total / 3.
marks = list(map(float, input("Marks of three subjects (out of 100 each): ").split()))
if len(marks) != 3 or any(m < 0 or m > 100 for m in marks):
    print("Enter exactly three marks from 0 to 100.")
else:
    total = sum(marks)
    percentage = total / 3
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(f"Total: {total:g}/300\nPercentage: {percentage:.2f}%\nGrade: {grade}")
