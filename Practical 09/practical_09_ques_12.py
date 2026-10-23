# Practical 9 - Question 12: Student result functions

# This function takes marks for three subjects and checks their range.
def read_marks():
    values = input("Marks of three subjects (0-100 each): ").split()
    if len(values) != 3:
        raise ValueError("Enter exactly three marks from 0 to 100.")

    first = float(values[0])
    second = float(values[1])
    third = float(values[2])
    if not (0 <= first <= 100 and 0 <= second <= 100 and 0 <= third <= 100):
        raise ValueError("Enter exactly three marks from 0 to 100.")
    return [first, second, third]


# I return the total and percentage so another function can use them.
def calculate(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage


def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


# I combine the input, calculation and grading functions here.
def main():
    try:
        marks = read_marks()
        total, percentage = calculate(marks)
    except ValueError as error:
        print(error)
        return

    grade = assign_grade(percentage)
    print(f"Total: {total:g}/300")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)


main()
