def count_subsets(arr, total):
    memo = {}
    return helper(arr, total, len(arr)-1)

def helper(arr, total, i, memo):
    key = str(total) + ":" + str(i)
    if key in memo:
        return memo[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = helper(arr, total, i -1)
    else:
        to_return = helper(arr, total - arr[i], i -1) + helper(arr, total, i-1)
    memo[key] = to_return
    return to_return