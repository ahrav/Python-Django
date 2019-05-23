def largest_sum(arr):
    if len(arr) == 0:
        return "Too small"

    max_sum = curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)

    return max_sum

print(largest_sum([1,2,3,78,65,-65,-23,4]))
print(4%7)


def largest_sum2(arr): ## with index
    if len(arr) == 0:
        return "Too small"

    max_sum = curr_sum = arr[0]
    curr_index = start_index = best_index = 0

    for num in range(1, len(arr)):
        if curr_sum + arr[num] > arr[num]:
            curr_sum = curr_sum + arr[num]
        else:
            curr_sum, curr_index = arr[num], num

        if curr_sum > max_sum:
            start_index, best_index, max_sum = curr_index, num+1, curr_sum 

    return arr[start_index: best_index]

print(largest_sum2([1,2,3,78,65,-65,-23,4]))
print(largest_sum2([-4, -65, 45, -23, 4, 30]))