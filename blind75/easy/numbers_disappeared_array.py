class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(range(1, len(nums) + 1))
        
        for i in nums:
            if i in nums_set:
                nums_set.remove(i)
                
        return nums_set

# TC: O(n)
# SC: O(n)


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        
        for i in nums:
            temp = abs(i)
            if nums[temp - 1] > 0:
                nums[temp - 1] *= -1

        for i, v in enumerate(nums):
            if v > 0:
                res.append(i + 1)
                
        return res

# TC: O(n)
# SC: O(1)

# Go thru all values in nums, mark its "sorted" place negative.  
# Numbers that are positive at the end are missing numbers