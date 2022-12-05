def max_profit(prices: list[int]) -> int:
    profit = 0
    for a in range(0, len(prices)-1):
        for b in range(a, len(prices)-1):
            if prices[a] < prices[b] and prices[b] - prices[a] > profit:
                profit = prices[b] - prices[a]
    return profit


c = [7,1,5,3,6,4]
print(max_profit(c))
