def array_manipulation(n, q):
    query_len = len(q)
    cache = [[0 for x in range(n)] for y in range(query_len+1)]
    max_num = 0
    for i in range(len(q)):
        start = q[i][0] - 1
        end = q[i][1] - 1
        operand = q[i][2]
        for j in range(n):
            if start <= j <= end and i == 0:
                cache[i][j] = operand
            if (j < start or j > end) and i == 0:
                cache[i][j] = 0
            if start <= j <= end and i != 0:
                cache[i][j] = cache[i-1][j]
                cache[i][j] = cache[i][j] + operand
                if cache[i][j] > max_num:
                    max_num = cache[i][j]
    return max_num





def array_manipulation2(n,q):
    cache = [0 for x in range(n)]
    for i in range(len(q)):
        start = q[i][0] - 1
        end = q[i][1] - 1
        operand = q[i][2]
        for x in cache[start:end+1]:
            cache[x] = cache[x] + operand
    return max(cache)


cache = [1,2,3,4,5]
for x in cache[1:3]:
    print (x)
