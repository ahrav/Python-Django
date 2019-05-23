def make_change(target, coin_list):
    min_coins = [0 for x in range(target+1)]
    for cents in range(target + 1):
        coin_count = cents
        for y in [coin for coin in coin_list if coin < cents]:
            if min_coins[cents - y]+1 < coin_count:
                coin_count = min_coins[cents - y]+1
            min_coins[cents] = coin_count
    return min_coins[target]