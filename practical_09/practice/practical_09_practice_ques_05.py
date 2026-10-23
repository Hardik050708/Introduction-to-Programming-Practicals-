# Practical 9 - Practice Question 5: Text sanitizer function

def sanitize(text):
    cleaned = " ".join(text.lower().split())  # Collapse all repeated whitespace.
    return cleaned, len(cleaned.split())

text, count = sanitize("Python   Makes   AI   Easy")
print("Cleaned:", text)
print("Word count:", count)
