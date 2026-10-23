# Practical 8 - Question 8: Character frequencies

text = input("Text: ")
frequency = {}
for character in text:
    frequency[character] = frequency.get(character, 0) + 1
print(frequency)  # Spaces and letter case are counted as entered.
