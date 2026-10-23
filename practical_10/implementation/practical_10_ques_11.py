# Practical 10 - Question 11: Palindrome by slicing

text = input("Text: ")
# Ignore letter case, spaces, and punctuation for phrase palindromes.
cleaned = "".join(character.lower() for character in text if character.isalnum())
if not cleaned:
    print("Enter at least one letter or digit.")
else:
    print("Palindrome" if cleaned == cleaned[::-1] else "Not a palindrome")
