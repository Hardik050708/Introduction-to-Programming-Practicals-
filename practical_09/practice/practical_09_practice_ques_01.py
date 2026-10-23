# Practical 9 - Practice Question 1: Average battery drop

def battery_drop(values):
    if len(values) < 2:
        raise ValueError("At least two hourly readings are required.")
    # Six readings contain five elapsed hourly intervals.
    return sum(values[i - 1] - values[i] for i in range(1, len(values))) / (len(values) - 1)

average = battery_drop([92, 88, 84, 79, 73, 68])
print(f"Average drop: {average:.2f} percentage points/hour")
print("Warning: drop exceeds 5% per hour" if average > 5 else "Drop is within 5% per hour")
