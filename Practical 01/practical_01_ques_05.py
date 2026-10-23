# Practical 1 - Question 5: Type casting inputs

# I first show the string-input error, then convert the inputs before calculating.

# First, I take the required input from the user.
age_text = input('Age: ')
marks_text = input('Marks: ')

# I use try-except so the expected error does not stop the example.
try:
    print(age_text + 1)
except TypeError:
    print('TypeError: a string cannot be added to an integer.')
try:
    age = int(age_text)
    marks = float(marks_text)
    # I add the values and store the answer in age_next_year.
    age_next_year = age + 1
    print('Age next year:', age_next_year)
    # I add the values and store the answer in marks_after_5_bonus_marks.
    marks_after_5_bonus_marks = marks + 5
    print('Marks after 5 bonus marks:', marks_after_5_bonus_marks)
except ValueError:
    print('Enter a whole-number age and numeric marks.')
