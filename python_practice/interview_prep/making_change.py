coins = [25,10,5,1]

def dp_change_maker(coins, change):
    min_coins = [0 for coin in range(change+1)]
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coins if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j]+1
        min_coins[cents] = coin_count
    return min_coins[change]


print (dp_change_maker(coins, 32))


def dynamic_change_maker(coin_list, change):
    ## make empty array for all possible coins
    min_coins = [0 for coin in range(change+1)]
    ## loop through all values until get to change value
    for cents in range(change+1):
        ## loop through all possible coin_list values less than or equal to cent currently on
        coin_count = cents
        for i in [c for c in coin_list <= cents]:
            if min_coins[cents - i] + 1 < coin_count:
                coin_count = min_coins[cents -i] + 1
        min_coins[cents] = coin_count
    return min_coins[change]