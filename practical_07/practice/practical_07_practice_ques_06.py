# Practical 7 - Practice Question 6: Slice quiz scores

# Slice into halves, then calculate maximum and average for each group.
scores = [78,85,91,88,76,95,89,84]
midterm, final = scores[:4], scores[-4:]
print("Midterm:", midterm)
print("Final:", final)
for label, values in (("Midterm", midterm), ("Final", final), ("Overall", scores)):
    print(f"{label} highest: {max(values)}; average: {sum(values) / len(values):.2f}")
