# Practical 8 - Viva Answers

**Question 1: What is a dictionary?**

It is a mutable mapping of unique, hashable keys to values.

**Question 2: Dictionary versus list?**

A dictionary retrieves by key; a list retrieves by integer position.

**Question 3: Why are dictionary keys unique?**

Each equal key identifies one entry, so assigning it again replaces that value.

**Question 4: What does get() do?**

It retrieves a value or returns a default instead of raising KeyError for a missing key.

**Question 5: What does update() do?**

It adds entries and replaces values for keys already present.

**Question 6: What is a nested dictionary?**

It is a dictionary containing other dictionaries as values.

**Question 7: How is a dictionary traversed?**

Iterate over the dictionary for keys, values() for values, or items() for pairs.

**Question 8: What if a duplicate key is added?**

The new value replaces the previous value for that key.

**Question 9: Why use dictionaries with JSON and APIs?**

Named fields map naturally to JSON objects and structured API responses.

**Question 10: When should a dictionary be preferred?**

Use it when named-key lookup and updating matter more than integer positions.
