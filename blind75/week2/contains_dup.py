class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        
        for i in nums:
            if i not in nums_counter:
                nums_set.add(i)
            else:
                return True
            
        return False

# Key: Use set instead of hash map (no need to keep track of anything other than value)
# TC: O(n)
# SC: O(1)