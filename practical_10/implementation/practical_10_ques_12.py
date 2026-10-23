# Practical 10 - Question 12: Text analyzer

import re
text = input("Paragraph: ")
# Treat runs of letters/digits as words; normalize case and ignore punctuation.
words = re.findall(r"[^\W_]+", text.lower())
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("Word count:", len(words))
print("Character count:", len(text))  # Includes spaces and punctuation.
if frequency:
    highest = max(frequency.values())
    print("Most frequent word(s):", [word for word in frequency if frequency[word] == highest])
    print("Frequency:", highest)
else:
    print("No words found.")
