# Practical 7 - Question 12: Shopping cart

# I use a list for changing cart items and a tuple for fixed categories.

categories = ('Food', 'Books', 'Stationery')
cart = ['Milk', 'Notebook']

# I add this item at the end of the list.
cart.append('Pen')

# I remove the first matching item.
cart.remove('Milk')

# I display the result clearly.
print('Fixed categories:', categories)
print('Cart:', cart)
print('Item count:', len(cart))
