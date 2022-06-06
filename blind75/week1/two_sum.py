class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [i, hash_map[target - nums[i]]]
            else:
                hash_map[nums[i]] = i
        
# Use hash map, storing number as KEY and index as VALUE.  This will be easier when trying to return the indexes at the end
# TC: O(n)
# SC: O(n)