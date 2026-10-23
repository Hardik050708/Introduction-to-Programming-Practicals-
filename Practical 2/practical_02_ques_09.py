# Practical 2 - Question 9: Three subject grading

# I validate the marks before calculating the total, percentage and grade.

# I start with an empty marks list.
marks = []

# I convert each separated input into a number before storing it.
for number_text in input('Marks of three subjects (out of 100 each): ').split():
    marks.append(float(number_text))
invalid_marks = False

# I repeat this step for each value in the sequence.
for m in marks:
    if m < 0 or m > 100:
        invalid_marks = True

# I check the input before using it in the calculation.
if len(marks) != 3 or invalid_marks:
    print('Enter exactly three marks from 0 to 100.')
else:
    total = sum(marks)
    # I divide the total by the number of subjects to get the percentage.
    percentage = total / 3
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 75:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'Fail'
    print(f'Total: {total:g}/300\nPercentage: {percentage:.2f}%\nGrade: {grade}')
