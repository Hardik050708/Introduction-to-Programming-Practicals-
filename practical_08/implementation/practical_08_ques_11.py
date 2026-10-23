# Practical 8 - Question 11: Sort dictionary data

# sorted orders pairs by key unless a value-based key function is supplied.
marks = {"Ravi": 85, "Asha": 92, "Neha": 78}
print("By keys:", dict(sorted(marks.items())))
print("By values:", dict(sorted(marks.items(), key=lambda item: item[1])))
