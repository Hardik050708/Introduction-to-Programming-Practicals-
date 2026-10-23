# Practical 6 - Practice Question 1: Soil moisture analysis

import numpy as np
moisture = np.array([[45,50,48,52,47,49,51], [55,53,54,52,56,57,55],
                     [38,40,42,39,41,43,44], [60,62,61,63,64,62,65]])
print("Zone averages:", moisture.mean(axis=1))
# Compare days using average moisture across all four zones.
daily = moisture.mean(axis=0)
print("Highest moisture day(s):", np.flatnonzero(daily == daily.max()) + 1)
print("Lowest moisture day(s):", np.flatnonzero(daily == daily.min()) + 1)
print("Highest day per zone:", moisture.argmax(axis=1) + 1)
print("Lowest day per zone:", moisture.argmin(axis=1) + 1)
