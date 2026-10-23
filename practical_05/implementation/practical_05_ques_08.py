# Practical 5 - Question 8: Three password attempts

PASSWORD = "python123"  # Demo password for the exercise.
for attempt in range(3):
    if input("Password: ") == PASSWORD:
        print("Access granted")
        break
    print("Incorrect password")
else:
    print("Access denied after 3 attempts")
