class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            lv = nums[m - 1] if m > 0 else float('-inf')
            rv = nums[m + 1] if m < len(nums) - 1 else float('inf')

            if lv < nums[m] > rv:
                return m
            elif lv < nums[m] < rv:
                l = m + 1
            else:
                r = m - 1
        
        return m