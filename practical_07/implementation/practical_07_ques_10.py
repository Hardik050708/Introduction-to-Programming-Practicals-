# Practical 7 - Question 10: List and tuple conversion

numbers = [1, 2, 3]
fixed = tuple(numbers)
print("Tuple:", fixed)
editable = list(fixed)
editable[0] = 10
print("Modified list:", editable)
print("Original tuple:", fixed)  # Converting creates a separate outer container.
