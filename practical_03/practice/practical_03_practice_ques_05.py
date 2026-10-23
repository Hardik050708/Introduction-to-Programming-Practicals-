# Practical 3 - Practice Question 5: Parking bill

from math import ceil
hours = float(input("Parking hours (0-24): "))
# Charge every started hour; zero hours is free, and the daily cap is INR 100.
if hours < 0 or hours > 24:
    print("Enter hours from 0 to 24 for one day.")
else:
    bill = 0 if hours == 0 else min(100, 20 + (ceil(hours) - 1) * 10)
    print(f"Parking bill: INR {bill:.2f}")
