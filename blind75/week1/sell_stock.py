class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        low = prices[0]
        
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                maxP = max(maxP, prices[i] - low)
                
        return maxP

# Key: keep track of the min.
# Update maximum if profit is bigger than current max
# TC: O(n)
# SC: O(1)