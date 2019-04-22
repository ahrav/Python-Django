def minimumBribes(arr):
    if arr == sorted(arr):
        return 0
    for num in range(len(arr)):
        bribes = 0
        if arr[num] >= num + 3 or arr[num] <= num - 3:
            return "Too Chaotic"
        else:
            if arr[num] == num + 2 or arr[num] == num - 2:
                bribes += 2
            if arr[num] == num + 1 or arr[num] == num - 1:
                bribes += 1
        return bribes

arr = [2,3,4,1,5]
print(minimumBribes(arr))