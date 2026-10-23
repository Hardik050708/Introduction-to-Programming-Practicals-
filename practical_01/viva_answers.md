# Practical 1 - Viva Answers

**Question 1: What is a variable, and how is it different from a constant?**

A variable names a value that may change; a constant is intended to stay fixed.

**Question 2: What are the variable naming rules?**

Use letters, digits and underscores, start without a digit, and avoid keywords: age_1 is valid; 1age and class are invalid.

**Question 3: What is dynamic typing?**

A name can refer to different types over time, such as x = 10 followed by x = "Python".

**Question 4: How is a data type identified automatically?**

The assigned object determines its type; 10 is int and 10.5 is float.

**Question 5: Implicit versus explicit conversion?**

Implicit conversion happens automatically, as in int + float; explicit conversion uses functions such as int().

**Question 6: Why cast input?**

input() returns text, so cast it before numeric arithmetic.

**Question 7: What does type() do?**

type(10) returns the class int, identifying the object type.

**Question 8: What does id() do?**

id() returns an object identity that stays unique among live objects; it is not a portable memory-address API.

**Question 9: How does + handle strings and numbers?**

Numbers are added, strings are concatenated, and mixing a number with a string requires conversion.
