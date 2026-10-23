# Practical 4 - Practice Question 4: Correct Fibonacci updates

a, b = 0, 1
for i in range(5):
    print(a)
    a, b = b, a + b  # Simultaneous assignment preserves the old a.
