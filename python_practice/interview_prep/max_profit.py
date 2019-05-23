def mox_profit(prices):
    if len(prices) < 2:
        return "Price list too short"
    max_profit = prices[1] - prices[0]
    min_price = prices[0]
    
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(profit, max_profit)
        min_price = min(price, min_price)

    return max_profit