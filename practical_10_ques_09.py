# Practical 10 - Question 9: Strip replace and format

text = "   Python is easy   "
cleaned = text.strip()  # strip removes whitespace only at the edges.
updated = cleaned.replace("easy", "powerful")
print(f"Cleaned: {cleaned}")
print(f"Updated: {updated}")
