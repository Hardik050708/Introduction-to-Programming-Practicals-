# Practical 10 - Question 11: Palindrome by slicing

# I remove punctuation and spaces, then compare the text with its reverse.

# For a phrase palindrome, I ignore punctuation, spaces and letter case.

# First, I take the required input from the user.
text = input('Text: ')
cleaned_text = ''

# I go through each character in the text.
for character in text:
    if character.isalnum():
        small_character = character.lower()
        # I add the valid character to the cleaned text.
        cleaned_text = cleaned_text + small_character

# I check this condition to decide which step should run.
if cleaned_text == '':
    print('Enter at least one letter or digit.')
else:
    # I use slicing to take the required part of the sequence.
    reversed_text = cleaned_text[::-1]
    # I compare the cleaned string with the reversed string.
    if cleaned_text == reversed_text:
        print('Palindrome')
    else:
        print('Not a palindrome')
