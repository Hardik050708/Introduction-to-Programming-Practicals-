# Practical 1 - Question 11: Celsius to Fahrenheit

# I use the Celsius-to-Fahrenheit formula after converting the input to float.

# First, I take the required input from the user.
celsius = float(input('Temperature in Celsius: '))

# I use F = C * 9 / 5 + 32 for the conversion.
fahrenheit = celsius * 9 / 5 + 32

# I display the result clearly.
print(f'{celsius:.2f} C = {fahrenheit:.2f} F')
