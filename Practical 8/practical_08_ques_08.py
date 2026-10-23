# Practical 8 - Question 8: Character frequencies

# I increase the count for each character as I go through the text.

# First, I take the required input from the user.
text = input('Text: ')
frequency = {}

# I go through each character in the text.
for character in text:
    # I add the values and store the answer in frequency[character].
    frequency[character] = frequency.get(character, 0) + 1

# I display the result clearly.
print(frequency)
