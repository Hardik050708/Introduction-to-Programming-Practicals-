# Practical 6 - Question 12: Student marks analysis

# I find each student average and compare the highest and lowest marks.

# I import NumPy because this question uses arrays.
import numpy as np

# I store the given values in a NumPy array.
marks = np.array([[80, 90, 70], [95, 85, 90], [60, 75, 65]])

# I display the result clearly.
print('Average per student:', marks.mean(axis=1))
print('Highest mark:', marks.max())
print('Lowest mark:', marks.min())
print('Highest per student:', marks.max(axis=1))
print('Lowest per student:', marks.min(axis=1))

# I add the values and store the answer in top_student_1_based.
top_student_1_based = int(marks.mean(axis=1).argmax()) + 1

# I display the result clearly.
print('Top student (1-based):', top_student_1_based)
