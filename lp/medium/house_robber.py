class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0 for i in range(len(nums) + 1)]
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[len(nums)]

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)
        
        dp = [-1] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[-1]
    
# Iterative - 2 variables, bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:

        a, b = 0, 0

        for n in nums:
            temp = max(a + n, b)
            a = b
            b = temp
        
        return b