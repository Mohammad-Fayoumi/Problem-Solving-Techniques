# --- Directions
# Given a string, return true if the string is a palindrome
# or false if it is not.  Palindromes are strings that
# form the same word if it is reversed. *Do* include spaces
# and punctuation in determining if the string is a palindrome.
# --- Examples:
#   palindrome("abba") === true
#   palindrome("abcdefg") === false

def is_palendrome(str):
    end = len(str) - 1
    start = 0

    while (start <= end):
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True


print(is_palendrome('annnnnnana'))

# T(n) = n/2