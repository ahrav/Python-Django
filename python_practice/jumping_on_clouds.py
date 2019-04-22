def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < len(c) - 1:
        if i <= (len(c) - 3):
            if c[i+2] != 1:
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1
    return count

c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))