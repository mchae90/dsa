class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                return True
                
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# TC: O(n)
# SC: O(n)