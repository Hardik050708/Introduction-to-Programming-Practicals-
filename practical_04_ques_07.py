# Practical 4 - Question 7: Count digits by parity

n = abs(int(input("Integer: ")))
total = even = odd = 0
# Zero itself has one even digit.
if n == 0:
    total = even = 1
while n > 0:
    digit = n % 10
    total += 1
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print("Total digits:", total)
print("Even digits:", even)
print("Odd digits:", odd)
