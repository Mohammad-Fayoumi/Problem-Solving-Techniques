def rotLeft(a, d):
    out = {}
    for i in range(0, len(a)):
        out[i] = 0
    for i in range(0, len(a)):
        new_pos = (i - d + len(a)) % len(a)
        print(a[i], new_pos)
        out[new_pos] = a[i]
    return out.values()
