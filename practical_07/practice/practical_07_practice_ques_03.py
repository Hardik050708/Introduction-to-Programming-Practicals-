# Practical 7 - Practice Question 3: Update doctor shift

shifts = [["Dr A","Dr B","Dr C"], ["Dr D","Dr E","Dr F"], ["Dr G","Dr H","Dr I"],
          ["Dr J","Dr K","Dr L"], ["Dr M","Dr N","Dr O"], ["Dr P","Dr Q","Dr R"],
          ["Dr S","Dr T","Dr U"]]
shifts[4][2] = "Dr Z"  # Day 5 is row 4; night is column 2.
for day, shift in enumerate(shifts, 1):
    print(f"Day {day}:", shift)
