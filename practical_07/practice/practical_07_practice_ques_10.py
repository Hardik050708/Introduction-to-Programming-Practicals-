# Practical 7 - Practice Question 10: Hostel room tuple

# count finds repetitions and index returns the first 0-based match.
rooms = ("A101","A102","A103","B201","B202","B203","C301","C302","C303","A101","B201")
print("A101 count:", rooms.count("A101"))
print("C302 index (0-based):", rooms.index("C302"))
repeated = sorted({room for room in rooms if rooms.count(room) > 1})
print("Repeated room IDs:", repeated)
floors = [room[0] for room in rooms]
print("Repeated floor categories:", sorted({floor for floor in floors if floors.count(floor) > 1}))
