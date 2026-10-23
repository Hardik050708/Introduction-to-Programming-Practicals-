# Practical 10 - Question 5: Membership searching

text = input("Text: ")
word = input("Substring to search: ")
print("Present" if word in text else "Absent")
print("Not present:", word not in text)  # Searches are case-sensitive.
