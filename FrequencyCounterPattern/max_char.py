# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"
from FrequencyCounterPattern.globle_scripts import frequency_counter

def max_char(str):
    fp = frequency_counter(str)
    max_char = ''
    max_char_count = 1

    for key in fp.keys():
        if fp[key] > max_char_count:
            max_char = key
            max_char_count = fp[key]
    return max_char

print(max_char("abcccccccd"))

# T(n) = n