# Practical 10 - Practice Question 1: Chatbot text normalization

# split and join collapse whitespace before lowercase and underscore formatting.
text = "   Python   makes   NLP   powerful   "
cleaned = " ".join(text.split()).lower()
words = cleaned.split()
print("Cleaned:", cleaned)
print("Words:", words)
print("Joined:", "_".join(words))
