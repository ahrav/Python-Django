def rotLeft(a, d):
    rot = a[:d]
    old = a[d:]
    new_arr = old + rot
    return new_arr

a = [1,2,3,4,5]
d = 4

print(rotLeft(a,d))

def array_left_rotation(a, d):
    for i in range(len(a)-1):
        f = a.pop(0)
        a.append(f)
    return a

print(array_left_rotation(a,d))