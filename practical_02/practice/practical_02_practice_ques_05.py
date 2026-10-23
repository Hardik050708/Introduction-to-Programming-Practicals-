# Practical 2 - Practice Question 5: Fuel cost

# Divide distance by mileage to get litres, then multiply by fuel price.
distance, mileage, price = 240, 15, 105
fuel = distance / mileage
print(f"Fuel needed: {fuel:.2f} litres")
print(f"Fuel cost: INR {fuel * price:.2f}")
