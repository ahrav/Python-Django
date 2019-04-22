def median_array(a,b):
    n = len(a)
    i = 0
    j = 0
    m1 = -1
    m2 = -1

    count = 0
    while count < n + 1:
        count += 1
        
        if i == n:
            m1 = m2
            m2 = b[0]

        elif j == n:
            m1 = m2
            m2 = a[0]

        if a[i] < b[j]:
            m1 = m2
            m2 = a[i]
            i += 1
        else:
            m1 = m2
            m2 = b[j]
            j += 1
    return (m1 + m2) / 2



ar1 = [1, 12, 15, 26, 38] 
ar2 = [2, 13, 17, 30, 45]

print (median_array(ar1, ar2))
