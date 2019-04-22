def minimumSwaps(arr):
    swaps = 0
    for i in range(0, len(arr)-1):
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            swaps += 1
            print(arr)

    return swaps


arr = [7,4,1,6,3,2,5]
print (minimumSwaps(arr))