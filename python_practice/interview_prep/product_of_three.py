def product(arr):
    high = max(arr[0], arr[i])
    low = min(arr[0], arr[1])
    high_prod2 = arr[0] * arr[1]
    low_prod2 = arr[0] * arr[1]
    high_prod3 = arr[0] * arr[1] * arr[2]
    
    for num in arr[2:]:
        high_prod3 = max(high_prod3, num*high_prod2, num*low_prod2)
        high_prod2 = max(high_prod2, num*high, num*low)
        low_prod2 = min(low_prod2, num*high, num*low)
        high = max(high, num)
        low = min(low, num)

    return high_prod3