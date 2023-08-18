class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        # l <= r will result in infinite loop
        while l < r:
            m = (l + r) // 2

            # we KNOW the pivot must be to the right of the middle
            if nums[m] > nums[r]:
                l = m + 1
            # we KNOW the pivot must be at m or to the left of middle
            else:
                r = m

        return nums[l]