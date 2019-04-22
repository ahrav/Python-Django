def three_sum(arr):
    results = []
    arr.sort()
    for i in range(len(arr)-3):
        if i == 0 or arr[i] > arr[i]-1:
            start = i + 1
            end = len(arr)-1
            while start < end:
                if arr[i] + arr[start] + arr[end] == 0:
                    results.append([arr[i], arr[start], arr[end]])
                if arr[i] + arr[start] + arr[end] < 0:
                    current_start = start
                    while arr[start] == arr[current_start] and start < end:
                        start += 1
                else:
                    current_end = end
                    while arr[end] == arr[current_end] and start < end:
                        end -= 1
    return results

print (three_sum([1,2,3,4,0,-1,-2,-3]))