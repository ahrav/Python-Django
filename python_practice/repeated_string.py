def repeatedString(s, n):
    if len(s) == 1:
        if s == 'a':
            return n
        else:
            return 0 
    string = n * s
    count = 0
    for letter in string[:n]:
        if letter == 'a':
            count += 1
    return count

print(repeatedString('adfsd', 100000000))