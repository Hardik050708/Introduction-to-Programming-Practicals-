# Practical 3 - Question 9: Triangle classification

# I take the three side lengths.
a, b, c = input("Three sides: ").split()
a = float(a)
b = float(b)
c = float(c)

# I check that the sides can form a triangle before comparing them.
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
