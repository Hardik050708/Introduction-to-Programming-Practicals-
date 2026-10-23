# Practical 5 - Practice Question 2: Skip duplicate RFID scans

# Track seen cards in a set and continue past repeated IDs.
seen = set()
for entry in range(60):
    card = input(f"RFID entry {entry + 1}/60: ").strip()
    if card in seen:
        continue
    seen.add(card)
    print("Attendance recorded:", card)
print("Unique attendance:", len(seen))
