# Practical 5 - Question 8: Three password attempts

# I allow three attempts and stop early when the password is correct.

PASSWORD = 'python123'

# I repeat this step for each value in the sequence.
for attempt in range(3):
    if input('Password: ') == PASSWORD:
        print('Access granted')
        # I stop this loop as soon as the required condition is met.
        break
    print('Incorrect password')
else:
    print('Access denied after 3 attempts')
