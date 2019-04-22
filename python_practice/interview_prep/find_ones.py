def find_ones(num):
    sum = 0
    while num > 0:
        sum += num & 1;
        num >>= 1
    return sum

print (find_ones(7))