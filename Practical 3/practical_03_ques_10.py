# Practical 3 - Question 10: Menu driven conditions

# Use the menu choice to select exactly one conditional branch.
print("1. Even/Odd\n2. Largest of three\n3. Grade")
choice = input("Choice: ").strip()
if choice == "1":
    n = int(input("Integer: "))
    print("Even" if n % 2 == 0 else "Odd")
elif choice == "2":
    a, b, c = map(float, input("Three numbers: ").split())
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)
elif choice == "3":
    marks = float(input("Marks (0-100): "))
    if not 0 <= marks <= 100:
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
