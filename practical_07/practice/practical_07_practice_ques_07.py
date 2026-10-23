# Practical 7 - Practice Question 7: Sort canteen combos

combos = [["Veg Burger",120], ["Pizza Slice",90], ["Pasta Bowl",150], ["Sandwich",80]]
combos.append(["Noodles", 110])
combos.sort(key=lambda item: item[1])  # Sort by price rather than meal name.
for meal, price in combos:
    print(f"{meal}: INR {price}")
