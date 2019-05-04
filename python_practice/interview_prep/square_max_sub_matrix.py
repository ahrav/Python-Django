def subarray(arr):
    x = len(arr)
    if x == 0:
        return 0
    y = len(arr[0])
    if y == 0:
        return 0
    max_sum = 0
    sizes = [[0 for x in range(x)] for y in range(y)]
    for i in range(len(x)):
        for j in range(len(y)):
            if i == 0 or j == 0:
                sizes[i][j] = arr[i][j]
            elif arr[i][j] == 1:
                sizes[i][j] = min(sizes[i][j-1],
                                  sizes[i-1][j],
                                  sizes[i-1][j-1]) + 1
            if sizes[i][j] > max_num:
                max_num = sizes[i][j]
    return max_num
