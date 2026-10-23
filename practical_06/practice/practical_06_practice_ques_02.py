# Practical 6 - Practice Question 2: ICU temperatures

import numpy as np
# The printed readings resemble Fahrenheit; preserve them without relabelling as Celsius.
temperatures = np.array([[98.6,99.1,100.2,99.8,98.9,99.0], [97.8,98.0,98.4,98.6,98.2,98.1],
                         [101.2,100.8,101.5,102.0,101.7,101.3], [99.4,99.5,99.6,99.3,99.2,99.1],
                         [98.7,98.9,99.0,98.8,98.6,98.5]])
print("Highest per patient:", temperatures.max(axis=1))
print("Average per patient:", temperatures.mean(axis=1))
print(f"Overall average: {temperatures.mean():.2f}")
# With no clinical threshold given, identify the patient with the highest peak.
critical = int(temperatures.max(axis=1).argmax())
print("Critical patient index (0-based):", critical)
print("Patient number (1-based):", critical + 1)
