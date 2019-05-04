def get_median(arr1, arr2, n):
    if n == 0:
        return -1
    if n == 1:
        return (arr1[0] + arr2[0]) / 2
    if n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        if m1 < m2:
            if n % 2 == 0:
                return get_median(arr1[(n//2 - 1):], arr2[:(n//2 + 1)], (n//2)+1)
            else:
                return get_median(arr1[n//2:], arr2[:(n//2 + 1)], (n//2)+1)
        else:
            if n  % 2 == 0:
                return get_median(arr2[(n//2 - 1):], arr1[:(n//2 + 1)], (n//2)+1)
            else:
                return get_median(arr2[n//2:], arr1[:(n//2 + 1)], (n//2)+1)
def median(arr, n):
        if n % 2 == 0:
            return (arr[n//2]) + (arr[(n//2 - 1)]) / 2
        else:
            return arr[n//2] 


ar1 = [1, 12, 15, 26, 38] 
ar2 = [2, 13, 17, 30, 45]
print (get_median(ar1, ar2, 5))