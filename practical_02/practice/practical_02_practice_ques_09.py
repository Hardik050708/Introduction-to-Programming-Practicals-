# Practical 2 - Practice Question 9: Restaurant bill sharing

# Add the percentage tip before dividing the bill among friends.
bill, friends, tip_rate = 1800, 4, 8
tip = bill * tip_rate / 100
total = bill + tip
print(f"Tip: INR {tip:.2f}\nFinal bill: INR {total:.2f}\nEach friend: INR {total / friends:.2f}")
