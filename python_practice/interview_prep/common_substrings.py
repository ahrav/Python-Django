def longest_substring(a,b):
    out = ""
    if len(a) == 0 or len(b) == 0:
        return out
    cache = [[0 for x in range(len(a))] for y in range(len(b))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i-1][j-1] + 1
                if cache[i][j] > len(out):
                    out = a[i - (cache[i][j]) +1 : i + 1]
    return out

x = 'abab'
y = 'baba'
print (longest_substring(x,y))


def longest_substring2(a, b):
    out = ""
    if not len(a) or not len(b):
        return out
    cache = [[0 for x in range(len(a))] for y in range(len(b))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i-1][j-1] + 1
                if cache[i][j] > len(out):
                    out = a[i - cache[i][j] + 1 : i + 1]
    return out