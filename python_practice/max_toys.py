def maximumToys(prices, k):
    count = 0
    total = 0
    prices.sort()
    for price in prices:
        if k - (total + price) >= 0:
            count += 1
            total += price
    return count


arr = [10,20,50,30,40]

print (maximumToys(arr, 30))