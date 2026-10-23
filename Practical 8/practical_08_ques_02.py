# Practical 8 - Question 2: Dictionary indexing

# Direct key access retrieves values and raises KeyError for a missing key.
student = {"name": "Asha", "age": 18, "marks": 92}

print("Name:", student["name"])
print("Marks:", student["marks"])
try:
    print(student["city"])
except KeyError:
    print("KeyError: city is not present.")
