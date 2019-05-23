def abs_sort(arr):
    arr.sort(key = lambda x: (abs(x), x>0))
    return arr

print(abs_sort([2, -7, -2, -2, 0]))