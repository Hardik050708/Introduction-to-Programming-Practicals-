# Practical 7 - Practice Question 5: Tuple calibration points

points = [(0,0), (10,5), (20,10), (30,15), (40,20)]
try:
    points[2][0] = 25
except TypeError:
    print("TypeError: individual tuple coordinates cannot be changed.")
points[2] = (25, 12)  # The containing list can replace a whole tuple.
print(points)
