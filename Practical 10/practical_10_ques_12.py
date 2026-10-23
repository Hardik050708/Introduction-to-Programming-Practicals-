# Practical 10 - Question 12: Text analyzer

# I take the paragraph and use the string methods covered in this practical.
text = input("Paragraph: ")
parts = text.lower().split()
words = []
frequency = {}

# I remove punctuation at the ends and count each word.
for part in parts:
    word = part.strip(".,!?;:\"'()[]{}")
    if word != "":
        words.append(word)
        frequency[word] = frequency.get(word, 0) + 1

word_count = len(words)
character_count = len(text)
print("Word count:", word_count)
print("Character count:", character_count)

# I find the highest count and collect the words having that count.
if word_count == 0:
    print("No words found.")
else:
    highest = max(frequency.values())
    most_frequent_words = []
    for word in frequency:
        if frequency[word] == highest:
            most_frequent_words.append(word)
    print("Most frequent word(s):", most_frequent_words)
    print("Frequency:", highest)
