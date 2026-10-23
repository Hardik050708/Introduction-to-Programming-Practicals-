# Practical 9 - Question 10: Local and global scope

# I compare a local assignment with a change made using global.

value = 10

# This assignment is local, so it does not change the outside value.
def local_change():
    value = 20
    print('Local:', value)

# I use global when I want to change the outside variable.
def global_change():
    global value
    value = 30
local_change()

# I display the result clearly.
print('Global after local change:', value)
global_change()
print('Global after global change:', value)
