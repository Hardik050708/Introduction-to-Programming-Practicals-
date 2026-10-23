# Practical 8 - Question 9: Nested dictionaries

# Use an outer student key followed by an inner detail key.
students = {"S101": {"name": "Asha", "marks": 92}, "S102": {"name": "Ravi", "marks": 85}}
print("S101 name:", students["S101"]["name"])
students["S102"]["marks"] = 90
print(students)
