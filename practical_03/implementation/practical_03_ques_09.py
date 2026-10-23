# Practical 3 - Question 9: Triangle classification

# Validate the triangle inequality before comparing side lengths.
a, b, c = map(float, input("Three sides: ").split())
if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
