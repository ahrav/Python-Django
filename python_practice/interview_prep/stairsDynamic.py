def num_ways(arr, n):
    if n == 0:
        return 1
    total = 0
    for i in arr:
        if n -i >= 0:
            total += num_ways(arr, n-i)
    return total


def num_ways_dp(arr, n):
    cache = [0] * (n+1)
    cache[0] = 1
    for i in range(1,n+1):
        total = 0
        for j in arr:
            if i-j >= 0:
                total += cache[i - j]
        cache[i] = total
    return cache[n]

print(num_ways_dp([2, 3, 5], 5))


# def make_change(change, coin_list):
#     min_coins = [0] * (change+1)
#     for cents in range(1,change+1):
#         coin_count = cents
#         for j in [coin for coin in coin_list if coin <= coin_count]:
#             if min_coins[coin_count - j] +1 < coin_count:
#                 coin_count = min_coins[cents - j] +1
#             min_coins[cents] = coin_count
#     return min_coins[change]

# print(make_change(11, [1, 5, 10, 25]))
