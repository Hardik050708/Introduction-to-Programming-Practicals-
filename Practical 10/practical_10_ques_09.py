# Practical 10 - Question 9: Strip replace and format

# I remove spaces at the ends, replace a word and format the result.

text = '   Python is easy   '
cleaned = text.strip()
updated = cleaned.replace('easy', 'powerful')

# I display the result clearly.
print(f'Cleaned: {cleaned}')
print(f'Updated: {updated}')
