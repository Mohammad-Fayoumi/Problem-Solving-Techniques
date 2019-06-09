# --- Directions
# Check to see if two provided strings are anagrams of each other.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation. Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False
import re


def clean_string(str):
    # Remove anything not alphpet
    # Use str.replace() and str.isalpha() inested of regex
    return ''.join(sorted(list(re.sub('[^A-Za-z0-9]+', '', str).lower())))


def anagrams(str1, str2):
    return clean_string(str1) == clean_string(str2)


print(anagrams('rail safety', 'fairy tales'))
print(anagrams('RAIL! SAFETY!', 'fairy tales'))
print(anagrams('Hi there', 'Bye there'))
