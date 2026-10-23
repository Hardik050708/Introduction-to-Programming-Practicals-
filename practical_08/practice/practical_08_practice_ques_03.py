# Practical 8 - Practice Question 3: Drone sensor dictionary

# Add the wind speed key and remove GPS before displaying the remaining pairs.
sensors = {"altitude":250, "speed":45, "battery":78, "gps":"ACTIVE"}
sensors["wind_speed"] = 12
sensors.pop("gps")
for key, value in sensors.items():
    print(key, value)
