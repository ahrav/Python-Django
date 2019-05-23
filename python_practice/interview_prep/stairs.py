def num_ways(n):
    if n <= 3:
        return n
    return num_ways(n-1) + num_ways(n-2)


print(num_ways(5))


def num_ways_dp(n):
    if n == 0 or n == 1:
        return 1
    result = [1, 1]
    for i in range(2,n+1):
        result.append(result[i-1] + result[i-2])
    return result.pop()


print(num_ways_dp(5))


def num_ways_best(num):
    a = 1
    b = 1
    if num == 0 or num == 1:
        return 1
    for i in range(2,num+1):
        c = b + a
        a = b
        b = c
    return b


print(num_ways_best(5))
