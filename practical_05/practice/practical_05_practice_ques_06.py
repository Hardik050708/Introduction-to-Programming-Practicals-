# Practical 5 - Practice Question 6: Average valid sensor readings

# Only nonnegative readings contribute to the total and valid-reading count.
readings = list(map(float, input("Temperature readings: ").split()))
total = count = 0
for value in readings:
    if value < 0:
        continue
    total += value
    count += 1
print("Average:", total / count if count else "No valid readings")
