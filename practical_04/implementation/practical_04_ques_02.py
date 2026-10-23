# Practical 4 - Question 2: While loop

# while repeats while its condition stays true; update prevents an infinite loop.
number = 1
while number <= 10:
    print(number, end=" ")
    number += 1
print("\nEquivalent for loop:")
for number in range(1, 11):
    print(number, end=" ")
print()
