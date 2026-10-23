# Practical 6 - Practice Question 4: Invert grayscale brightness

# Subtract each pixel from 255 to invert its grayscale brightness.
import numpy as np
image = np.array([[120,135,140,150,160,170], [110,125,130,145,155,165],
                  [100,115,120,135,145,155], [90,105,110,125,135,145],
                  [80,95,100,115,125,135], [70,85,90,105,115,125]])
inverted = 255 - image
print("Inverted image:\n", inverted)
