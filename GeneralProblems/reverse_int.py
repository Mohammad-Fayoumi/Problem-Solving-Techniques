# --- Directions
# Given an integer, return an integer that is the reverse
# ordering of numbers.
# --- Examples
#   reverseInt(15) === 51
#   reverseInt(981) === 189
#   reverseInt(500) === 5
#   reverseInt(-15) === -51
#   reverseInt(-90) === -9

def reverse_int(num):
    sign = -1
    reversed = ''
    if num < 0:
        sign = -1
        num *= -1
    for n in str(num):
        reversed = n + reversed
    if not sign:
        return int(reversed) * sign
    return int(reversed)

print(reverse_int(12450021110))

# T(n) = n