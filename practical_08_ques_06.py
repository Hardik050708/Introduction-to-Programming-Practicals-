# Practical 8 - Question 6: Dictionary iteration

# Iterate through keys, values, or items depending on the required output.
student = {"name": "Asha", "age": 18, "marks": 92}

print("Keys:")
for key in student:
    print(key)
print("Values:")
for value in student.values():
    print(value)
print("Pairs:")
for key, value in student.items():
    print(key, value)
