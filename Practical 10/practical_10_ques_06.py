# Practical 10 - Question 6: Find and index

text = "Python makes programming easy"
print("find programming:", text.find("programming"))
print("index programming:", text.index("programming"))
print("find missing:", text.find("Java"))  # find returns -1 when absent.
try:
    print(text.index("Java"))
except ValueError:
    print("index missing: ValueError")  # index raises an error when absent.
