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
    
