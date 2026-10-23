# Practical 1 - Question 7: Memory and mutability

a = b = 10
print("Before:", a, b, id(a), id(b))
a += 1
print("After:", a, b, id(a), id(b))
# Integers are immutable; rebinding a leaves b unchanged.
x = y = [10]
x.append(20)
print("Shared mutable list:", x, y)
# Both names still refer to the same list after mutation.
