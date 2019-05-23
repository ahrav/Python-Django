import math
import random

def reorder(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        pick = int(math.floor((i +1)* random.random()))
        arr[i], arr[pick] = arr[pick], arr[i]
    return arr


print(reorder([1, 0, 4, 5, 3]))

