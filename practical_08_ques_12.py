# Practical 8 - Question 12: Inventory system

# Add, update, and remove product keys to maintain inventory quantities.
inventory = {"Pen": 20, "Notebook": 10}
inventory["Pencil"] = 15
inventory["Pen"] += 5
inventory.pop("Notebook")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")
