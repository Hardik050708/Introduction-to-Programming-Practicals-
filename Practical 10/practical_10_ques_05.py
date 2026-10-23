# Practical 10 - Question 5: Membership searching

# I use in and not in to check whether the substring is present.

# The substring search is case-sensitive.

# First, I take the required input from the user.
text = input('Text: ')
word = input('Substring to search: ')

# I check this condition to decide which step should run.
if word in text:
    search_result = 'Present'
else:
    search_result = 'Absent'

# I display the result clearly.
print(search_result)
print('Not present:', word not in text)
