# Practical 5 - Question 10: Pattern with skipped even values

# continue skips even values inside each row of the nested pattern.
rows = int(input("Rows: "))
for row in range(1, rows + 1):
    for value in range(1, row + 1):
        if value % 2 == 0:
            continue
        print(value, end=" ")
    print()
