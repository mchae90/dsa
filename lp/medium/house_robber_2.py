class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):
            a = 0
            b = 0

            for n in arr:
                temp = max(a + n, b)
                a = b
                b = temp
            
            return b
        
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))
    

class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(helper(nums[1:]), helper(nums[:-1]))