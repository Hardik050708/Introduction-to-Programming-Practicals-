# Practical 4 - Question 6: Reverse and palindrome

# I reverse the digits one at a time and compare with the original number.

# First, I take the required input from the user.
n = int(input('Nonnegative integer: '))

# I check the input before using it in the calculation.
if n < 0:
    print('Enter a nonnegative integer.')
else:
    original = n
    # I start reverse at zero before counting or adding anything.
    reverse = 0
    # I repeat the steps until the stopping condition is reached.
    while n > 0:
        # I add the values and store the answer in reverse.
        reverse = reverse * 10 + n % 10
        n //= 10
    print('Reverse:', reverse)
    if original == reverse:
        palindrome_result = 'Palindrome'
    else:
        palindrome_result = 'Not a palindrome'
    print(palindrome_result)
