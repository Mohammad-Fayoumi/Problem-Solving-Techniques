def frequency_counter(str):
    fq = {}
    for char in str:
        if char in fq.keys():
            fq[char] += 1
        else:
            fq[char] = 1
    return fq