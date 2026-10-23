# Practical 6 - Question 12: Student marks analysis

# axis=1 computes per-student results across subject columns.
import numpy as np
marks = np.array([[80, 90, 70], [95, 85, 90], [60, 75, 65]])
print("Average per student:", marks.mean(axis=1))
print("Highest mark:", marks.max())
print("Lowest mark:", marks.min())
print("Highest per student:", marks.max(axis=1))
print("Lowest per student:", marks.min(axis=1))
print("Top student (1-based):", int(marks.mean(axis=1).argmax()) + 1)
