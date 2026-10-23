# Practical 7 - Practice Question 2: Unpack drone coordinates

# Tuple unpacking separates each coordinate into x, y, and altitude.
points = [(10,20,150), (15,25,160), (20,30,170), (25,35,180), (30,40,190),
          (35,45,200), (40,50,210), (45,55,220), (50,60,230), (55,65,240)]
for i, (x, y, altitude) in enumerate(points, 1):
    print(f"Checkpoint {i}: x={x}, y={y}, altitude={altitude}")
