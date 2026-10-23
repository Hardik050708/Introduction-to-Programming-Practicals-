# Practical 5 - Question 4: Search a list

numbers = list(map(int, input("Numbers separated by spaces: ").split()))
target = int(input("Search number: "))
for i, number in enumerate(numbers):
    if number == target:
        print("Position:", i + 1)  # Display the first match using 1-based position.
        break
else:
    print("Not found")
