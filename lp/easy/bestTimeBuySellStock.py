class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        
        low = prices[0]
        
        for i in prices:
            if i < low:
                low = i
            else:
                profit = i - low
                maxP = max(maxP, profit)
        
        return maxP

TC: O(n)
SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        g_min = prices[0]
        res = 0

        for p in prices:
            g_min = min(g_min, p)
            res = max(res, p - g_min)
        
        return res