# Iterative
class Solution:
    def climbStairs(self, n: int) -> int:

        a, b = 1, 1
        
        for _ in range(n):
            temp = a + b
            a = b
            b = temp
            
        return a

# TC: O(n)
# SC: O(1)

# DP - memoization
class Solution:
    def __init__(self):
        self.memo = {}
    
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        
        if n in self.memo:
            return self.memo[n]
        
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        self.memo[n] = res
        
        return res
        
# Dynamic Programming - tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]