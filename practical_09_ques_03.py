# Practical 9 - Question 3: Return a square

def square(number):
    return number * number  # return passes the result back to the caller.

number = float(input("Number: "))
result = square(number)
print("Square:", result)
print("Square plus one:", result + 1)
