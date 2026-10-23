# Practical 7 - Practice Question 8: GPS route slicing

# The manual says 20 points but prints only these 10; use the supplied data.
route = [(18.5204,73.8567), (18.5210,73.8575), (18.5221,73.8580), (18.5232,73.8591),
         (18.5243,73.8602), (18.5254,73.8613), (18.5265,73.8624), (18.5276,73.8635),
         (18.5287,73.8646), (18.5298,73.8657)]
print("Alternate checkpoints:", route[::2])
print("First five:", route[:5])
print("Reverse route:", route[::-1])
