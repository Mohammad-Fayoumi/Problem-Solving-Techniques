# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') === 'leppa'
#   reverse('hello') === 'olleh'
#   reverse('Greetings!') === '!sgniteerG'

def reverse_string(str):
    reversed = ''
    for char in str:
        reversed = char + reversed
    return reversed

print(reverse_string('apple'))

# T(n) = n