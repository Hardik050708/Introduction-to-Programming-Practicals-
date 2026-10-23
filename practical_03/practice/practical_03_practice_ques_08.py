# Practical 3 - Practice Question 8: Recharge benefits

# Check the highest recharge threshold first.
amount = int(input("Recharge amount (whole rupees): "))
if amount < 0:
    print("Invalid amount")
elif amount >= 299:
    print("2 GB/day")
elif amount >= 199:
    print("1 GB/day")
else:
    print("Talktime only")
