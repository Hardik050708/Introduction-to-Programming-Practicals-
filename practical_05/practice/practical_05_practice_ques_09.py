# Practical 5 - Practice Question 9: Skip weekend analysis

# Assume day 1 is Monday; remainders 5 and 6 represent Saturday and Sunday.
for day in range(1, 31):
    if (day - 1) % 7 in (5, 6):
        continue
    print("Analyzing day", day)
