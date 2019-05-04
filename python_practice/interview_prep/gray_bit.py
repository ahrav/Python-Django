def is_gray(a,b):
    c = a ^ b
    while c > 0:
        if c % 2 == 1 and c >> 1 > 0:
            return False
        c = c >> 1
    return True

def is_gray2(a,b):
    x = a ^ b
    return (x & (x-1)) == 0

print (is_gray(7,10))