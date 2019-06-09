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
from FrequencyCounterPattern.globle_scripts import frequency_counter


def clean_string(str):
    # Remove anything not alphpet
    # Use str.replace() and str.isalpha() inested of regex
    return re.sub('[^A-Za-z0-9]+', '', str).lower()


def anagrams(str1, str2):
    str1 = clean_string(str1)
    str2 = clean_string(str2)

    if len(str1) != len(str2):
        return False
    freq_count1 = frequency_counter(str1)
    freq_count2 = frequency_counter(str2)

    # Compare each key with its value in 2 dictionaries
    for char in freq_count1.keys():
        if char not in freq_count2.keys() or freq_count1[char] != freq_count2[char]:
            return False
    return True


print(anagrams('rail safety', 'fairy tales'))
print(anagrams('RAIL! SAFETY!', 'fairy tales'))
print(anagrams('Hi there', 'Bye there'))
