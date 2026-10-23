# Practical 10 - Question 4: String immutability

text = "python"
try:
    text[0] = "P"
except TypeError:
    print("TypeError: strings cannot be changed in place.")
text = "P" + text[1:]  # Build a new string instead of changing a character.
print("Corrected:", text)
