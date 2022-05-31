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

# Key: two pointers - l (buy), r (sell)
# increment r buy 1 every iteration.  Update maximum if profit is bigger than current max
# TC: O(n)
# SC: O(1)