# Practical 8 - Practice Question 5: Word frequencies

# Count each word by incrementing its existing dictionary value.
text = "python makes coding easy and python makes debugging easier"
frequency = {}
for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)
