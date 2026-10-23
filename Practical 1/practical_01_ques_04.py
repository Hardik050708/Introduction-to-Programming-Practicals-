# Practical 1 - Question 4: Data type identification

# I take each input and convert it to the required data type.
number = int(input("Integer: "))
decimal = float(input("Float: "))
text = input("String: ")
boolean_text = input("Boolean (true/false): ").strip().lower()

# I compare the Boolean text because bool("false") would also be True.
if boolean_text == "true" or boolean_text == "false":
    flag = boolean_text == "true"

    # I print a summary table directly, without a loop.
    print(f"{'Value':<20} Type")
    print(f"{number:<20} {type(number).__name__}")
    print(f"{decimal:<20} {type(decimal).__name__}")
    print(f"{text:<20} {type(text).__name__}")
    print(f"{str(flag):<20} {type(flag).__name__}")
else:
    print("Enter true or false for the Boolean.")
