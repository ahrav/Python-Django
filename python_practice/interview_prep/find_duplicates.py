##O(N) runtime and O(1) space

## only if number between 1 and len of array

def find_duplicates(arr):
    result = set()
    for i in range(len(arr)):
        index = abs(arr[i] - 1)
        if arr[index] < 0:
            result.add(abs(arr[index]))
        else:
            arr[index] = -arr[index]
    ## just for code clean up leave the list as it was
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    return list(result)