# Practical 8 - Question 12: Inventory system

# I add a product, update stock and remove an item from the inventory.

inventory = {'Pen': 20, 'Notebook': 10}
inventory['Pencil'] = 15
inventory['Pen'] += 5
inventory.pop('Notebook')

# I repeat this step for each value in the sequence.
for product, quantity in inventory.items():
    print(f'{product}: {quantity}')
