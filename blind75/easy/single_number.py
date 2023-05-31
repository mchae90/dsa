class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i in nums:
            res ^= i
        
        return res

# XOR on same two numbers will result in 0.
# XOR 0 to itself will result in number itself.

# TC: O(n)
# SC: O(1)