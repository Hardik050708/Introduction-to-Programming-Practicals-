# Practical 1 - Question 3: Constants simulation

# Uppercase names signal constants by convention, without enforcement.
PI, GRAVITY, MAX_USERS = 3.14159, 9.8, 100
print("Original:", PI, GRAVITY, MAX_USERS)
PI = 3.14
print("Reassignment is allowed:", PI)
# Treat these uppercase values as read-only in normal use.
AREA_PI = 3.14159
print("Circle area for radius 2:", AREA_PI * 2 ** 2)
