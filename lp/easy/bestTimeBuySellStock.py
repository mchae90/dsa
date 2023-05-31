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