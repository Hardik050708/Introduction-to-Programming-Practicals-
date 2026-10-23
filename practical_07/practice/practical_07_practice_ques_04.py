# Practical 7 - Practice Question 4: Deduplicate play history

songs = ["Shape of You","Believer","Perfect","Believer","Faded","Perfect","Senorita",
         "Levitating","Faded","Perfect","Blinding Lights","Senorita","Peaches","Believer","Perfect"]
unique = []
for song in songs:
    if song not in unique:
        unique.append(song)  # Preserve each song's first appearance.
print(unique)
