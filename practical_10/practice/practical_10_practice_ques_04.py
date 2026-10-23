# Practical 10 - Practice Question 4: Password validation

password = "PySecure2026!"
MIN_LENGTH = 8  # The manual does not specify a minimum; use 8 characters.
checks = {
    "Uppercase": any(c.isupper() for c in password),
    "Lowercase": any(c.islower() for c in password),
    "Digit": any(c.isdigit() for c in password),
    "Special character": any(not c.isalnum() and not c.isspace() for c in password),
    "Minimum length": len(password) >= MIN_LENGTH,
}
for rule, passed in checks.items():
    print(f"{rule}: {passed}")
print("Valid password:", all(checks.values()))
