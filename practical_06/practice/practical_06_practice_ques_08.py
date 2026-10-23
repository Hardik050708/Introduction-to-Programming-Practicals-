# Practical 6 - Practice Question 8: Weighted retail revenue

# Multiply each category sale by its weight and sum for each store.
import numpy as np
sales = np.array([[100,120,130,140,150], [110,125,135,145,155], [90,100,110,120,130],
                  [80,95,105,115,125], [70,85,95,105,115], [60,75,85,95,105], [50,65,75,85,95]])
weights = np.array([2, 3, 1, 4, 5])
revenue = sales @ weights
for store, value in enumerate(revenue, 1):
    print(f"Store {store} weighted revenue: {value}")
