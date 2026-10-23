# Practical 7 - Question 12: Shopping cart

# Use a changing list for cart items and a fixed tuple for categories.
categories = ("Food", "Books", "Stationery")
cart = ["Milk", "Notebook"]
cart.append("Pen")
cart.remove("Milk")
print("Fixed categories:", categories)
print("Cart:", cart)
print("Item count:", len(cart))
