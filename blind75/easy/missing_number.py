class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i, v in enumerate(nums):
            res ^= i + 1
            res ^= v
        
        return res

# XOR all numbers in range and all numbers in nums.  
# Missing number will manifest itself since XOR two same numbers result in 0
# TC: O(n)
# SC: O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        return (n * (n + 1) // 2) - sum(nums)

# Gaussian sum minus sum of nums (missing the number).  Result is missing number
# TC: O(n)
# SC: O(1)