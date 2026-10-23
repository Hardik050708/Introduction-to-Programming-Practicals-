# Practical 1 - Question 10: Boolean logic

# Store comparison results as Booleans and combine them with and.
age = int(input("Age: "))
marks = float(input("Marks: "))
is_adult = age > 18
has_passed = marks > 50
print("Age > 18:", is_adult)
print("Marks > 50:", has_passed)
if is_adult and has_passed:
    print("Both conditions are satisfied.")
else:
    print("At least one condition is false.")
