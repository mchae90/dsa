class Solution:
    def climbStairs(self, n: int) -> int:

        a, b = 1, 1
        
        for _ in range(n):
            temp = a + b
            a = b
            b = temp
            
        return a

        