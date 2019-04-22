def countingValleys(n, s):
    start = 0
    valleys = False
    count = 0
    i = 0
    while i < n:
        if start == 0:
            valleys = False
        if s[i] == 'D':
            start -= 1
            if start < 0 and valleys is False:
                count += 1
                valleys = True
                i += 1
            else:
                i += 1
        else:
            start += 1
            if start > 0 and valleys is True:
                valleys = False
                i += 1
            else:
                i += 1
    return count

s = 'DDUUDDUDUUUD'
n = 12
print (countingValleys(n,s))