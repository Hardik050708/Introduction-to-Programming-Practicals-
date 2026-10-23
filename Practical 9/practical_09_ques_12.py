# Practical 9 - Question 12: Student result functions

# I combine separate functions for reading marks, calculating results and grading.

# I read and validate the marks before returning them.
def read_marks():
    # I start with an empty marks list.
    marks = []
    # I convert each separated input into a number before storing it.
    for number_text in input('Marks of three subjects (0-100 each): ').split():
        marks.append(float(number_text))
    invalid_marks = False
    # I repeat this step for each value in the sequence.
    for mark in marks:
        if mark < 0 or mark > 100:
            invalid_marks = True
    # I check the input before using it in the calculation.
    if len(marks) != 3 or invalid_marks:
        raise ValueError('Enter exactly three marks from 0 to 100.')
    # I return the result so it can be used by the calling code.
    return marks

# I return both the total and percentage for the given marks.
def calculate(marks):
    # I start total at zero before counting or adding anything.
    total = 0
    # I repeat this step for each value in the sequence.
    for mark in marks:
        # I add the values and store the answer in total.
        total = total + mark
    # I divide the total by the number of subjects to get the percentage.
    percentage = total / len(marks)
    # I return the result so it can be used by the calling code.
    return (total, percentage)

# I select the grade by comparing the percentage with each cutoff.
def assign_grade(percentage):
    if percentage >= 90:
        return 'A'
    if percentage >= 75:
        return 'B'
    if percentage >= 50:
        return 'C'
    return 'Fail'

# I call the required functions here in the correct order.
def main():
    # I use try-except so the expected error does not stop the example.
    try:
        marks = read_marks()
        total, percentage = calculate(marks)
    except ValueError as error:
        print(error)
        return
    grade = assign_grade(percentage)
    print(f'Total: {total:g}/300\nPercentage: {percentage:.2f}%\nGrade: {grade}')

# I call main() to start the complete program.
main()
