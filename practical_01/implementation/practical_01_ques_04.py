# Practical 1 - Question 4: Data type identification

number = int(input("Integer: "))
decimal = float(input("Float: "))
text = input("String: ")
answer = input("Boolean (true/false): ").strip().lower()
# bool("False") is True, so parse the words explicitly.
if answer not in ("true", "false"):
    print("Enter true or false for the Boolean.")
else:
    flag = answer == "true"
    print(f"{'Value':<20} Type")
    for value in (number, decimal, text, flag):
        print(f"{str(value):<20} {type(value).__name__}")
