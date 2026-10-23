# Practical 2 - Question 9: Three subject grading

# I take the marks of three subjects, each out of 100.
marks = input("Marks of three subjects (out of 100 each): ").split()

if len(marks) != 3:
    print("Enter exactly three marks from 0 to 100.")
else:
    first_marks = float(marks[0])
    second_marks = float(marks[1])
    third_marks = float(marks[2])

    # I check each mark directly instead of using a loop.
    if not (0 <= first_marks <= 100 and 0 <= second_marks <= 100 and 0 <= third_marks <= 100):
        print("Enter exactly three marks from 0 to 100.")
    else:
        total = first_marks + second_marks + third_marks
        percentage = total / 3

        # I use the grade ranges given in the manual's grading example.
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print(f"Total: {total:g}/300")
        print(f"Percentage: {percentage:.2f}%")
        print("Grade:", grade)
