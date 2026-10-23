# Practical 8 - Question 5: Remove dictionary entries

# pop returns the removed value; del removes an entry without returning it.
student = {"name": "Asha", "age": 18, "marks": 92}

print("Removed marks:", student.pop("marks"))
del student["age"]
print("Remaining:", student)
try:
    del student["city"]
except KeyError:
    print("KeyError: city is absent.")
print("Safe missing pop:", student.pop("city", "Not found"))
