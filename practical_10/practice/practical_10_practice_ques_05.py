# Practical 10 - Practice Question 5: Medical keyword analyzer

# Count whole symptom words and find the one with the highest frequency.
report = "fever cough fever fatigue fever cold"
words = report.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("Fever occurrences:", frequency.get("fever", 0))
print("Unique symptoms:", list(frequency))
print("Unique symptom count:", len(frequency))
print("Most repeated symptom:", max(frequency, key=frequency.get))
