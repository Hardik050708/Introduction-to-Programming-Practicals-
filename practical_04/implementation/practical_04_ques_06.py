# Practical 4 - Question 6: Reverse and palindrome

n = int(input("Nonnegative integer: "))
if n < 0:
    print("Enter a nonnegative integer.")
else:
    original, reverse = n, 0
    while n > 0:
        reverse = reverse * 10 + n % 10  # Append the last digit.
        n //= 10
    print("Reverse:", reverse)
    print("Palindrome" if original == reverse else "Not a palindrome")
