# Practical 6 - Practice Question 3: Classroom occupancy

# Sum occupied slots per room and count zeros to find unused slots.
import numpy as np
rooms = np.array([[1,1,0,1,0,1,1,0], [1,0,1,1,1,0,1,1], [0,1,1,0,1,1,0,1],
                  [1,1,1,1,0,0,1,0], [0,0,1,1,1,1,1,1]])
occupied = rooms.sum(axis=1)
print("Busiest room(s):", np.flatnonzero(occupied == occupied.max()) + 1)
print("Total free slots:", int((rooms == 0).sum()))
print(f"Occupancy: {rooms.mean() * 100:.2f}%")
