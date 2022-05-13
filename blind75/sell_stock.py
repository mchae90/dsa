def maxProfit(prices):
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
        else:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        r += 1
    return maxP