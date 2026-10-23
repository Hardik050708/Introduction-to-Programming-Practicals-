# Practical 2 - Practice Question 2: Average speed

# Average speed equals distance divided by elapsed time.
distance = float(input("Distance (km): "))
time = float(input("Time (hours): "))
if distance < 0 or time <= 0:
    print("Distance must be nonnegative and time must be positive.")
else:
    print(f"Average speed: {distance / time:.2f} km/h")
