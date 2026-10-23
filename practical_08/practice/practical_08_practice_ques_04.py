# Practical 8 - Practice Question 4: Retail inventory

stock = {"Laptop":12, "Mouse":40, "Keyboard":25, "Monitor":10}
stock["Laptop"] -= 2
stock["Printer"] = 5
# Iterate over a key copy because entries may be deleted.
for product in list(stock):
    if stock[product] == 0:
        del stock[product]
print(stock)
