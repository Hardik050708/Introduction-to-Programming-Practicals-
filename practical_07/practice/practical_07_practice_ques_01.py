# Practical 7 - Practice Question 1: Library return queue

books = [1045,1098,1120,1087,1155,1178,1201,1199,1180,1166,1134,1102]
# The front is newest; the final entry is the oldest.
books.insert(0, 1215)
print("Removed oldest:", books.pop())
print("Updated returns:", books)
