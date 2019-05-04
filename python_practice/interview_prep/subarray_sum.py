def find_zero_sum(arr):
    dict = {}
    sum = 0
    for num in range(len(arr)):
        sum += arr[num]
        keys = dict.keys()
        if sum in keys:
            start = dict[sum]
            return arr[start+1: num +1]
        elif sum == 0:
            return arr[0:num+1]
        else:
            dict[sum] = num
    return None

print (find_zero_sum([1,-1]))