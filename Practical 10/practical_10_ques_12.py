# Practical 10 - Question 12: Text analyzer

# I count the words and characters and keep all words tied for highest frequency.

# Character count includes spaces and punctuation; word count ignores punctuation.

import re

# First, I take the required input from the user.
text = input('Paragraph: ')
words = re.findall('[^\\W_]+', text.lower())
frequency = {}

# I go through each word in the text.
for word in words:
    # I add the values and store the answer in frequency[word].
    frequency[word] = frequency.get(word, 0) + 1

# I display the result clearly.
print('Word count:', len(words))
print('Character count:', len(text))

# I check this condition to decide which step should run.
if frequency:
    highest = max(frequency.values())
    # I start with an empty most frequent words list.
    most_frequent_words = []
    # I go through each word in the text.
    for word in frequency:
        if frequency[word] == highest:
            most_frequent_words.append(word)
    print('Most frequent word(s):', most_frequent_words)
    print('Frequency:', highest)
else:
    print('No words found.')
