def change(arr, change):
    result = []

    for i in range(len(arr)-1, -1, -1):
        while change >= arr[i]:
            change = change - arr[i]
            result.append(arr[i])

    return result

print(change([1, 5, 10, 25], 33))
