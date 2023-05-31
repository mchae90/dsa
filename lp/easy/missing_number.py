# Hash Table method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(range(0, len(nums) + 1))
        
        for i in nums:
            if i in nums_set:
                nums_set.remove(i)
        
        return nums_set.pop()
        
TC: O(n)
SC: O(n)


# XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
            
        return res

TC: O(n)
SC: O(1)