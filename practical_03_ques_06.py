# Practical 3 - Question 6: Leap year

# Century years need divisibility by 400; other years need divisibility by 4.
year = int(input("Year: "))
if year <= 0:
    print("Enter a positive year.")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
