def product(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    output = [None] * len(arr)
    product = 1
    i = 0
    while i < len(arr):
        output[i] = product
        product *= arr[i]
        i += 1
    i = len(arr) -1
    product = 1
    while i <= 0:
        output[i] *= product
        product = arr[i]
        i -= 1
    return output
    