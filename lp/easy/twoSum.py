class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}
        
        for i, v in enumerate(nums):
            if target - v not in nums_d:
                nums_d[v] = i
            else:
                return [nums_d[target - v], i]

TC: O(n)
SC: O(n)