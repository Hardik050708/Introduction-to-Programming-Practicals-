# Practical 9 - Question 12: Student result functions

# Separate input, percentage calculation, and grading into reusable functions.
def read_marks():
    marks = list(map(float, input("Marks of three subjects (0-100 each): ").split()))
    if len(marks) != 3 or any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Enter exactly three marks from 0 to 100.")
    return marks

def calculate(marks):
    return sum(marks), sum(marks) / len(marks)

def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 75:
        return "B"
    if percentage >= 50:
        return "C"
    return "Fail"

def main():
    try:
        total, percentage = calculate(read_marks())
    except ValueError as error:
        print(error)
        return
    print(f"Total: {total:g}/300\nPercentage: {percentage:.2f}%\nGrade: {assign_grade(percentage)}")

main()
