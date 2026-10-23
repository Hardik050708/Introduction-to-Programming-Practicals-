# Practical 6 - Practice Question 6: Traffic reshape

import numpy as np
counts = np.array([120,135,140,150,160,155,148,170,180,175,190,200,
                   210,205,198,220,230,225,240,250,245,238,230,220])
traffic = counts.reshape(3, 8)  # Interpret the requested shape as 3 junctions x 8 slots.
print("Traffic matrix:\n", traffic)
print("Peak [junction, slot] (1-based):", np.argwhere(traffic == traffic.max()) + 1)
print("Peak traffic count:", traffic.max())
print("Least busy junction:", int(traffic.sum(axis=1).argmin()) + 1)
print(f"Average count: {traffic.mean():.2f}")
