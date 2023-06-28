class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')

        # l to r
        prod = 1
        for n in nums:
            prod *= n
            res = max(res, prod)
            if n == 0:
                prod = 1
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            res = max(res, prod)
            if nums[i] == 0:
                prod = 1
        
        return res