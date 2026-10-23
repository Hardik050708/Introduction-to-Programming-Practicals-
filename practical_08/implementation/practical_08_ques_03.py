# Practical 8 - Question 3: Safe get method

student = {"name": "Asha", "age": 18, "marks": 92}

print("Name:", student.get("name"))
print("City:", student.get("city", "Unknown"))
# get returns a default for missing keys; direct indexing raises KeyError.
