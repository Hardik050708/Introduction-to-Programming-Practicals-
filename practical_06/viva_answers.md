# Practical 6 - Viva Answers

**Question 1: 1D versus 2D arrays?**

A 1D array has one index axis; a 2D array has row and column axes.

**Question 2: How do nested lists represent a matrix?**

The outer list holds rows and each inner list holds that row's values.

**Question 3: Why use NumPy?**

It provides efficient numeric storage, vectorized arithmetic, and multidimensional operations.

**Question 4: How does 2D slicing work?**

NumPy uses array[row_slice, column_slice]; nested lists need separate per-row slicing.

**Question 5: What is matrix traversal?**

It visits matrix elements in an order such as row-wise or column-wise.

**Question 6: Why use reshape()?**

It changes array dimensions without changing the number of elements.

**Question 7: What if multiplication dimensions do not match?**

Matrix multiplication raises ValueError when the left column count differs from the right row count.

**Question 8: How are row and column sums calculated?**

For NumPy arrays, sum(axis=1) gives row sums and sum(axis=0) gives column sums.

**Question 9: Why transpose data?**

Transposing exchanges rows and columns for calculations, tables, or feature arrangement.

**Question 10: Why are arrays useful in AI?**

They organize numeric datasets, images, and model inputs for efficient computation.
