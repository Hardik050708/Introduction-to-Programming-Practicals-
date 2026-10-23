# Practical 6 - Practice Question 10: Terrain elevation

import numpy as np
rng = np.random.default_rng(42)
terrain = rng.integers(100, 501, size=(10, 10))
print("Highest ridge elevation:", terrain.max())
print("Ridge coordinates (0-based):", np.argwhere(terrain == terrain.max()))
print("Lowest valley elevation:", terrain.min())
print("Valley coordinates (0-based):", np.argwhere(terrain == terrain.min()))
print(f"Average elevation: {terrain.mean():.2f} m")
print("Central 4x4:\n", terrain[3:7, 3:7])  # Indices 3 through 6 select the center.
