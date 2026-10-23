# Practical 7 - Practice Question 9: Stock prices and positions

prices = [210,215,208,220,225,230,218,240,235,245]
# Keep each value paired with its original 1-based time slot.
top = sorted(enumerate(prices, 1), key=lambda item: item[1], reverse=True)[:3]
for slot, price in top:
    print(f"Price: {price}; position: {slot}")
print("Lowest price slot:", prices.index(min(prices)) + 1)
