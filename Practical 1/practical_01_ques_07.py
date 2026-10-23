# Practical 1 - Question 7: Memory and mutability

# I compare object IDs to see how assignment and list changes behave.

# Integers are immutable, while a shared list can be changed in place.

a = 10
b = a

# I display the result clearly.
print('Before:', a, b, id(a), id(b))
a += 1
print('After:', a, b, id(a), id(b))
x = [10]
y = x

# I add this item at the end of the list.
x.append(20)

# I display the result clearly.
print('Shared mutable list:', x, y)
