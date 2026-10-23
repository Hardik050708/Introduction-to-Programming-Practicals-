# Practical 8 - Question 12: Inventory system

# I store each product name with its quantity.
inventory = {"Pen": 20, "Notebook": 10}

# I add a product, update the stock and remove a product in separate steps.
inventory["Pencil"] = 15
inventory["Pen"] = inventory["Pen"] + 5
inventory.pop("Notebook")

print("Final inventory:", inventory)
