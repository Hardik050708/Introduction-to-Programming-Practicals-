# Practical 3 - Question 5: Largest of three

# I take three numbers and convert each input separately.
a, b, c = input("Three numbers: ").split()
a = float(a)
b = float(b)
c = float(c)

# I use if-elif-else, and >= also handles equal largest values.
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
