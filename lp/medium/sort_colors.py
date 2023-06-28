# Bucket sort - two passes
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0, 0, 0]

        for n in nums:
            count[n] += 1
        
        place = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[place] = i
                place += 1

        return nums
    
# Two pointer partition - one pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
            i += 1