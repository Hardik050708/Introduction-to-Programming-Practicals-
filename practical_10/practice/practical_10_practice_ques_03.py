# Practical 10 - Practice Question 3: Flight log parser

# Split fields at pipes, then split each field at the colon.
log = "ALT:250|SPD:45|BAT:78"
values = {}
for item in log.split("|"):
    key, value = item.split(":")
    values[key] = int(value)
print("Altitude:", values["ALT"])
print("Speed:", values["SPD"])
print("Battery:", values["BAT"])
