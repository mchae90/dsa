# sort the array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

# use set
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hset = set()

        for n in nums:
            if n in hset:
                return n
            hset.add(n)

