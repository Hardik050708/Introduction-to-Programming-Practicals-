# Practical 2 - Question 7: Unit conversion

km = float(input("Distance (km): "))
celsius = float(input("Temperature (C): "))
rupees = float(input("Amount (INR): "))
INR_PER_USD = 83.0  # Fixed classroom rate, not a live exchange rate.
print(f"{km} km = {km * 1000:.2f} m")
print(f"{celsius} C = {celsius * 9 / 5 + 32:.2f} F")
print(f"INR {rupees:.2f} = USD {rupees / INR_PER_USD:.2f}")
