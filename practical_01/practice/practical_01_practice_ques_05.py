# Practical 1 - Practice Question 5: Convert a decimal string

# int("12.5") fails; float() preserves the decimal value.
num = float("12.5")
print(num)
print("Truncated integer:", int(num))
