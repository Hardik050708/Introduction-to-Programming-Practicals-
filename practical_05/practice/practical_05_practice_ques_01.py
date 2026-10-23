# Practical 5 - Practice Question 1: Drone battery scan

# break stops scanning as soon as a battery reading falls below 15.
batteries = list(map(float, input("Battery percentages by row: ").split()))
for row, battery in enumerate(batteries, 1):
    if battery < 15:
        print("Scan stopped at row", row)
        break
    print("Scanned row", row)
