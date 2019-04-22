def sockMerchant(n, arr):
    pairs = {}
    for x in arr:
        if x not in pairs:
            pairs[x] = 1
        else:
            pairs[x] += 1
    total_pairs = 0
    for sock, count in pairs.items():
        if count % 2 == 0:
            pair = count // 2
            total_pairs += pair
        if count % 2 == 1:
            pair = count // 2
            total_pairs += pair
    return total_pairs

arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
# print(sockMerchant(n, arr))

def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count

print(sockMerchant(n, arr))