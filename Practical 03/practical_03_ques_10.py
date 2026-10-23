# Practical 3 - Question 10: Menu driven conditions

# I display the three choices given in the question.
print("1. Even/Odd")
print("2. Largest of three")
print("3. Grade")
choice = input("Choice: ").strip()

# I use if-elif to run only the selected operation.
if choice == "1":
    number = int(input("Integer: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif choice == "2":
    a, b, c = input("Three numbers: ").split()
    a = float(a)
    b = float(b)
    c = float(c)

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print("Largest:", largest)

elif choice == "3":
    marks = float(input("Marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Fail")

else:
    print("Invalid choice")
