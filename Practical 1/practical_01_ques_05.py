# Practical 1 - Question 5: Type casting inputs

age_text = input("Age: ")
marks_text = input("Marks: ")
# input() returns strings, so numeric operations require casting.
try:
    print(age_text + 1)
except TypeError:
    print("TypeError: a string cannot be added to an integer.")
try:
    age, marks = int(age_text), float(marks_text)
    print("Age next year:", age + 1)
    print("Marks after 5 bonus marks:", marks + 5)
except ValueError:
    print("Enter a whole-number age and numeric marks.")
