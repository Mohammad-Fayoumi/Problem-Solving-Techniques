# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

def chunk(array, size):
    if len(array) < size:
        return array
    chunks = []
    start = 0
    while start <= len(array):
        chunks.append(array[start:start + size])
        start += size
    return chunks


print(chunk([1, 2, 3, 4, 5, 6, 7, 8], 3))

# n = length
# T(n) = n/size
# Best case length = size T(n) = 1
# Worst case size = 1 T(n) = length = n