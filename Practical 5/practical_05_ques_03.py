# Practical 5 - Question 3: Compare break and continue

print("break:")
for n in range(1, 11):
    if n == 5:
        break
    print(n, end=" ")
print("\ncontinue:")
for n in range(1, 11):
    if n == 5:
        continue
    print(n, end=" ")
print()
# break ends the loop; continue skips only 5 and resumes at 6.
