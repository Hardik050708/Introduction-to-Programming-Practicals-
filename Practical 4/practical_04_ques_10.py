# Practical 4 - Question 10: Nested loop patterns

# The outer loop selects the row and the inner loop prints its elements.
rows = int(input("Rows: "))
if rows < 1:
    print("Rows must be positive.")
else:
    print("Star triangle:")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()
    print("Reverse star triangle:")
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
    print("Number triangle:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print("Reverse number triangle:")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
