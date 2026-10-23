# Practical 10 - Question 11: Palindrome by slicing

# I take the string and reverse it using slicing, as asked in the manual.
text = input("Text: ")
reversed_text = text[::-1]

# I compare the entered string directly with its reverse.
if text == "":
    print("Enter a nonempty string.")
elif text == reversed_text:
    print("Palindrome")
else:
    print("Not a palindrome")
