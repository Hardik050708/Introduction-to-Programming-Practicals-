# Practical 9 - Question 10: Local and global scope

value = 10

def local_change():
    value = 20  # A local binding does not change the global variable.
    print("Local:", value)

def global_change():
    global value
    value = 30

local_change()
print("Global after local change:", value)
global_change()
print("Global after global change:", value)
