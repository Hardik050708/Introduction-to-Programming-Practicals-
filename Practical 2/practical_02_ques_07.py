# Practical 2 - Question 7: Unit conversion

# I convert the given values and display the correct units with each answer.

# I use a fixed classroom rate of INR 83 per USD.

# First, I take the required input from the user.
km = float(input('Distance (km): '))
celsius = float(input('Temperature (C): '))
rupees = float(input('Amount (INR): '))
INR_PER_USD = 83.0

# I display the result clearly.
print(f'{km} km = {km * 1000:.2f} m')
print(f'{celsius} C = {celsius * 9 / 5 + 32:.2f} F')
print(f'INR {rupees:.2f} = USD {rupees / INR_PER_USD:.2f}')
