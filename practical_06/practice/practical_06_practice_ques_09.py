# Practical 6 - Practice Question 9: Rainfall trends

import numpy as np
rng = np.random.default_rng(42)  # Fixed seed makes the example repeatable.
rainfall = rng.integers(20, 121, size=(8, 30))
first, last = rainfall[:, :15], rainfall[:, 15:]
print("First-half district averages:", first.mean(axis=1))
print("Last-half district averages:", last.mean(axis=1))
print(f"First-half overall average: {first.mean():.2f} mm")
print(f"Last-half overall average: {last.mean():.2f} mm")
print("Change per district:", last.mean(axis=1) - first.mean(axis=1))
print("Wetter half:", "First" if first.mean() > last.mean() else "Last" if last.mean() > first.mean() else "Equal")
