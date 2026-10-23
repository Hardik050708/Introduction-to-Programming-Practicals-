# Practical 5 - Practice Question 5: PIN retry limit

PIN = "123456"  # Store as text so a PIN can retain leading zeros.
failures = 0
while True:
    entered = input("6-digit PIN: ")
    if entered.isascii() and entered.isdigit() and len(entered) == 6 and entered == PIN:
        print("Unlocked")
        break
    failures += 1
    if failures == 5:
        print("Locked after 5 failed attempts")
        break
    print("Incorrect PIN; retry.")
