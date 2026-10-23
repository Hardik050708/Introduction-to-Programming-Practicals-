# Practical 1 - Question 6: Implicit and explicit conversion

# int + float automatically produces a float.
print("Implicit:", 5 + 2.5, type(5 + 2.5))
try:
    print(5 + "2")
except TypeError:
    print("TypeError: int + string needs an explicit conversion.")
print("Numeric addition:", 5 + int("2"))
print("String joining:", str(5) + "2")
