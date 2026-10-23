# Practical 3 - Question 5: Largest of three

a, b, c = map(float, input("Three numbers: ").split())
# >= handles ties without excluding equal largest values.
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest:", largest)
